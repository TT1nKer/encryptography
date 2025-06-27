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

    # No longer save public.pem

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
    del aes_key
    return privkey_path, enc_aes_key_path, enc_file_path

def run_packager_thread(self):
    def task():
        try:
            privkey_path, enc_aes_key_path, enc_file_path = package_executable_with_progress(
                self.file_path, self.enc_dir, self.privkey_dir, self.update_status)
            self.status_label.config(text='Done!')
            messagebox.showinfo('Success', f'Packaging complete!\n\nprivate.pem: {privkey_path}\nencrypted_aes_key.bin: {enc_aes_key_path}\nencrypted_program.bin: {enc_file_path}')
        except Exception as e:
            messagebox.showerror('Error', f'Packaging failed: {e}')
        finally:
            self.status_label.grid_remove()

    self.packager_thread = threading.Thread(target=task)
    self.packager_thread.start()

enc_dir_label = tk.Label(frame, text='Save encrypted files to:')
enc_dir_label.grid(row=1, column=0, sticky='e') 