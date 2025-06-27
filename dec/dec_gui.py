import tkinter as tk
from tkinter import filedialog, messagebox
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad
import threading


def decrypt_file(enc_file, enc_aes_key_file, privkey_file, output_file, status_callback=None):
    try:
        if status_callback:
            status_callback('Loading private key...')
        with open(privkey_file, 'rb') as f:
            private_key = RSA.import_key(f.read())

        if status_callback:
            status_callback('Loading and decrypting AES key...')
        with open(enc_aes_key_file, 'rb') as f:
            enc_aes_key = f.read()
        cipher_rsa = PKCS1_OAEP.new(private_key)
        aes_key = cipher_rsa.decrypt(enc_aes_key)

        if status_callback:
            status_callback('Decrypting file...')
        with open(enc_file, 'rb') as fin:
            iv = fin.read(16)
            cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
            enc_data = fin.read()
            data = unpad(cipher_aes.decrypt(enc_data), AES.block_size)
        with open(output_file, 'wb') as fout:
            fout.write(data)
        if status_callback:
            status_callback('Decryption complete!')
        messagebox.showinfo('Success', f'Decryption complete!\nOutput: {output_file}')
    except Exception as e:
        if status_callback:
            status_callback('Error!')
        messagebox.showerror('Error', f'Decryption failed: {e}')


def run_decrypt_thread():
    enc_file = enc_file_entry.get()
    enc_aes_key_file = enc_aes_key_entry.get()
    privkey_file = privkey_entry.get()
    output_file = output_entry.get()
    if not all([enc_file, enc_aes_key_file, privkey_file, output_file]):
        messagebox.showerror('Error', 'Please fill in all fields.')
        return
    status_label.config(text='Starting...')
    status_label.grid()
    def update_status(msg):
        status_label.config(text=msg)
        frame.update_idletasks()
    def task():
        decrypt_file(enc_file, enc_aes_key_file, privkey_file, output_file, update_status)
        status_label.grid_remove()
    threading.Thread(target=task).start()


def browse_file(entry, filetypes=None):
    path = filedialog.askopenfilename(filetypes=filetypes)
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def browse_save_file(entry):
    path = filedialog.asksaveasfilename()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

# --- GUI Setup ---
root = tk.Tk()
root.title('File Decryptor (Encryptography)')
root.geometry('1200x300')

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill=tk.BOTH, expand=True)

# Encrypted file
enc_file_label = tk.Label(frame, text='Encrypted file (encrypted_program.bin):')
enc_file_label.grid(row=0, column=0, sticky='e')
enc_file_entry = tk.Entry(frame, width=50)
enc_file_entry.grid(row=0, column=1, padx=5)
enc_file_browse = tk.Button(frame, text='Browse...', command=lambda: browse_file(enc_file_entry))
enc_file_browse.grid(row=0, column=2)

# Encrypted AES key
enc_aes_key_label = tk.Label(frame, text='Encrypted AES key (encrypted_aes_key.bin):')
enc_aes_key_label.grid(row=1, column=0, sticky='e')
enc_aes_key_entry = tk.Entry(frame, width=50)
enc_aes_key_entry.grid(row=1, column=1, padx=5)
enc_aes_key_browse = tk.Button(frame, text='Browse...', command=lambda: browse_file(enc_aes_key_entry))
enc_aes_key_browse.grid(row=1, column=2)

# Private key
privkey_label = tk.Label(frame, text='Private key (private.pem):')
privkey_label.grid(row=2, column=0, sticky='e')
privkey_entry = tk.Entry(frame, width=50)
privkey_entry.grid(row=2, column=1, padx=5)
privkey_browse = tk.Button(frame, text='Browse...', command=lambda: browse_file(privkey_entry))
privkey_browse.grid(row=2, column=2)

# Output file
output_label = tk.Label(frame, text='Output file:')
output_label.grid(row=3, column=0, sticky='e')
output_entry = tk.Entry(frame, width=50)
output_entry.grid(row=3, column=1, padx=5)
output_browse = tk.Button(frame, text='Browse...', command=lambda: browse_save_file(output_entry))
output_browse.grid(row=3, column=2)

# Status label
status_label = tk.Label(frame, text='')
status_label.grid(row=5, column=0, columnspan=3)
status_label.grid_remove()

# Run button
run_btn = tk.Button(frame, text='Decrypt File', command=run_decrypt_thread, bg='#2196F3', fg='white', height=2)
run_btn.grid(row=4, column=0, columnspan=3, pady=20, sticky='ew')

root.mainloop() 