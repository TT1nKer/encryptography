import argparse
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def package_executable_with_progress(file_path, enc_dir, privkey_dir):
    print('[*] Generating RSA key pair...')
    key = RSA.generate(4096)
    private_key_pem = key.export_key()
    public_key_pem = key.publickey().export_key()

    print('[*] Saving private.pem...')
    privkey_path = os.path.join(privkey_dir, 'private.pem')
    with open(privkey_path, 'wb') as f:
        f.write(private_key_pem)

    # Save public key in the encrypted files directory
    public_key_path = os.path.join(enc_dir, 'public.pem')
    with open(public_key_path, 'wb') as f:
        f.write(public_key_pem)

    print('[*] Generating AES key and encrypting it...')
    public_key = RSA.import_key(public_key_pem)
    aes_key = get_random_bytes(32)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_aes_key = cipher_rsa.encrypt(aes_key)

    enc_aes_key_path = os.path.join(enc_dir, 'encrypted_aes_key.bin')
    with open(enc_aes_key_path, 'wb') as f:
        f.write(enc_aes_key)

    print('[*] Encrypting file...')
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
            percent = int(processed * 100 / total_chunks)
            print(f'    Encrypting chunk {processed}/{total_chunks}... ({percent}%)', end='\r')
    print('\n[*] Done!')
    # For security: AES key is only in memory and never saved in plaintext.
    del aes_key
    return privkey_path, public_key_path, enc_aes_key_path, enc_file_path


def main():
    parser = argparse.ArgumentParser(description='Encrypt a file with AES, protect the key with RSA, and save outputs securely.')
    parser.add_argument('--file', help='Path to the file to encrypt')
    parser.add_argument('--enc_dir', help='Directory to save encrypted files and public key')
    parser.add_argument('--privkey_dir', help='Directory to save private.pem')
    args = parser.parse_args()

    file_path = args.file
    enc_dir = args.enc_dir
    privkey_dir = args.privkey_dir

    if not file_path:
        file_path = input('Please enter the path of the file to encrypt: ').strip()
    if not enc_dir:
        enc_dir = input('Please enter the directory to save encrypted files and public key: ').strip()
    if not privkey_dir:
        privkey_dir = input('Please enter the directory to save private.pem: ').strip()

    if not os.path.isfile(file_path):
        print(f'[!] File not found: {file_path}')
        return
    if not os.path.isdir(enc_dir):
        print(f'[!] Encrypted files directory not found: {enc_dir}')
        return
    if not os.path.isdir(privkey_dir):
        print(f'[!] Private key directory not found: {privkey_dir}')
        return

    privkey_path, public_key_path, enc_aes_key_path, enc_file_path = package_executable_with_progress(
        file_path, enc_dir, privkey_dir)
    print('\n[+] Packaging complete!')
    print(f'    private.pem: {privkey_path}')
    print(f'    public.pem: {public_key_path}')
    print(f'    encrypted_aes_key.bin: {enc_aes_key_path}')
    print(f'    encrypted_program.bin: {enc_file_path}')

if __name__ == '__main__':
    main() 