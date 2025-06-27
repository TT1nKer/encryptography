import argparse
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import unpad


def decrypt_file(enc_file, enc_aes_key_file, privkey_file, output_file):
    print('[*] Loading private key...')
    with open(privkey_file, 'rb') as f:
        private_key = RSA.import_key(f.read())

    print('[*] Loading and decrypting AES key...')
    with open(enc_aes_key_file, 'rb') as f:
        enc_aes_key = f.read()
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(enc_aes_key)

    print('[*] Decrypting file...')
    with open(enc_file, 'rb') as fin:
        iv = fin.read(16)
        cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
        enc_data = fin.read()
        data = unpad(cipher_aes.decrypt(enc_data), AES.block_size)
    with open(output_file, 'wb') as fout:
        fout.write(data)
    print(f'[+] Decryption complete! Output: {output_file}')


def main():
    parser = argparse.ArgumentParser(description='Decrypt a file encrypted with enc.py or enc_gui.py.')
    parser.add_argument('--enc_file', required=True, help='Path to encrypted_program.bin')
    parser.add_argument('--enc_aes_key', required=True, help='Path to encrypted_aes_key.bin')
    parser.add_argument('--privkey', required=True, help='Path to private.pem')
    parser.add_argument('--output', required=True, help='Path to save the decrypted file')
    args = parser.parse_args()

    decrypt_file(args.enc_file, args.enc_aes_key, args.privkey, args.output)

if __name__ == '__main__':
    main() 