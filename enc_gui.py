import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import sys
import threading


def package_executable_with_progress(file_path, enc_dir, privkey_dir, status_callback=None):
    if status_callback:
        status_callback('Generating RSA key pair...')
    key = RSA.generate(4096)
    private_key_pem = key.export_key()
    public_key_pem = key.publickey().export_key()

    if status_callback:
        status_callback('Saving private.pem...')
    privkey_path = os.path.join(privkey_dir, 'private.pem')
    with open(privkey_path, 'wb') as f:
        f.write(private_key_pem)

    # Save public key in the encrypted files directory
    public_key_path = os.path.join(enc_dir, 'public.pem')
    with open(public_key_path, 'wb') as f:
        f.write(public_key_pem)

    if status_callback:
        status_callback('Generating AES key and encrypting it...')
    public_key = RSA.import_key(public_key_pem)
    aes_key = get_random_bytes(32)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_aes_key = cipher_rsa.encrypt(aes_key)

    enc_aes_key_path = os.path.join(enc_dir, 'encrypted_aes_key.bin')
    with open(enc_aes_key_path, 'wb') as f:
        f.write(enc_aes_key)

    if status_callback:
        status_callback('Encrypting file...')
    file_size = os.path.getsize(file_path)
    chunk_size = 128 * 1024  # 128KB for more updates
    total_chunks = (file_size + chunk_size - 1) // chunk_size
    processed = 0
    enc_file_path = os.path.join(enc_dir, 'encrypted_program.bin')
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    iv = cipher_aes.iv
    with open(file_path, 'rb') as fin, open(enc_file_path, 'wb') as fout:
        fout.write(iv)  # Write IV first
        while True:
            chunk = fin.read(chunk_size)
            if not chunk:
                break
            if fin.tell() == file_size:
                # Last chunk, pad it
                chunk = pad(chunk, AES.block_size)
            enc_chunk = cipher_aes.encrypt(chunk)
            fout.write(enc_chunk)
            processed += 1
            if status_callback:
                status_callback(f'Encrypting chunk {processed}/{total_chunks}...')
    # For security: AES key is only in memory and never saved in plaintext.
    return privkey_path, public_key_path, enc_aes_key_path, enc_file_path


def run_packager_thread():
    file_path = file_entry.get()
    enc_dir = enc_dir_entry.get()
    privkey_dir = privkey_entry.get()
    if not file_path or not os.path.isfile(file_path):
        messagebox.showerror('Error', 'Please select a valid file to encrypt.')
        return
    if not enc_dir or not os.path.isdir(enc_dir):
        messagebox.showerror('Error', 'Please select a valid folder to save encrypted files.')
        return
    if not privkey_dir or not os.path.isdir(privkey_dir):
        messagebox.showerror('Error', 'Please select a valid folder for the private key.')
        return
    status_label.config(text='Starting...')
    status_label.grid()
    def update_status(msg):
        status_label.config(text=msg)
        frame.update_idletasks()
    def task():
        try:
            privkey_path, public_key_path, enc_aes_key_path, enc_file_path = package_executable_with_progress(
                file_path, enc_dir, privkey_dir, update_status)
            status_label.config(text='Done!')
            messagebox.showinfo('Success', f'Packaging complete!\n\nprivate.pem: {privkey_path}\npublic.pem: {public_key_path}\nencrypted_aes_key.bin: {enc_aes_key_path}\nencrypted_program.bin: {enc_file_path}')
        except Exception as e:
            messagebox.showerror('Error', f'Packaging failed: {e}')
        finally:
            status_label.grid_remove()
    threading.Thread(target=task).start()


def browse_privkey_dir():
    path = filedialog.askdirectory(title='Select folder for private.pem')
    if path:
        privkey_entry.delete(0, tk.END)
        privkey_entry.insert(0, path)


def browse_file():
    path = filedialog.askopenfilename(title='Select file to encrypt', filetypes=[('All files', '*.*')])
    if path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, path)


def open_privkey_folder():
    path = privkey_entry.get()
    if path and os.path.isdir(path):
        if sys.platform == 'win32':
            os.startfile(path)
        elif sys.platform == 'darwin':
            os.system(f'open "{path}"')
        else:
            os.system(f'xdg-open "{path}"')


def browse_enc_dir():
    path = filedialog.askdirectory(title='Select folder to save encrypted files and public key')
    if path:
        enc_dir_entry.delete(0, tk.END)
        enc_dir_entry.insert(0, path)


def open_enc_dir():
    path = enc_dir_entry.get()
    if path and os.path.isdir(path):
        if sys.platform == 'win32':
            os.startfile(path)
        elif sys.platform == 'darwin':
            os.system(f'open "{path}"')
        else:
            os.system(f'xdg-open "{path}"')


# --- GUI Setup ---
root = tk.Tk()
root.title('File Packager (Encryptography)')
root.geometry('1000x300')

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# File selection
file_label = tk.Label(frame, text='File to encrypt:')
file_label.grid(row=0, column=0, sticky='e')
file_entry = tk.Entry(frame, width=40)
file_entry.grid(row=0, column=1, padx=5)
file_browse = tk.Button(frame, text='Browse...', command=browse_file)
file_browse.grid(row=0, column=2)

# Encrypted files directory selection
enc_dir_label = tk.Label(frame, text='Save encrypted files and public key to:')
enc_dir_label.grid(row=1, column=0, sticky='e')
enc_dir_entry = tk.Entry(frame, width=40)
enc_dir_entry.grid(row=1, column=1, padx=5)
enc_dir_browse = tk.Button(frame, text='Browse...', command=browse_enc_dir)
enc_dir_browse.grid(row=1, column=2)
enc_dir_open = tk.Button(frame, text='Open', command=open_enc_dir)
enc_dir_open.grid(row=1, column=3, padx=5)

# Private key folder selection
privkey_label = tk.Label(frame, text='Save private.pem to:')
privkey_label.grid(row=2, column=0, sticky='e')
privkey_entry = tk.Entry(frame, width=40)
privkey_entry.grid(row=2, column=1, padx=5)
privkey_browse = tk.Button(frame, text='Browse...', command=browse_privkey_dir)
privkey_browse.grid(row=2, column=2)
privkey_open = tk.Button(frame, text='Open', command=open_privkey_folder)
privkey_open.grid(row=2, column=3, padx=5)

# Status label
status_label = tk.Label(frame, text='')
status_label.grid(row=4, column=0, columnspan=4)
status_label.grid_remove()

# Run button
run_btn = tk.Button(frame, text='Package File', command=run_packager_thread, bg='#4CAF50', fg='white', height=2)
run_btn.grid(row=3, column=0, columnspan=4, pady=20, sticky='ew')

root.mainloop() 