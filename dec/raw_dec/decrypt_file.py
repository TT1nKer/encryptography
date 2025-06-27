from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import sys
import os

# 用法: python decrypt_file.py encrypted_program.bin decrypted_aes_key.bin output_file
# Usage: python decrypt_file.py encrypted_program.bin decrypted_aes_key.bin output_file
if len(sys.argv) != 4:
    print('用法: python decrypt_file.py encrypted_program.bin decrypted_aes_key.bin output_file')
    print('Usage: python decrypt_file.py encrypted_program.bin decrypted_aes_key.bin output_file')
    sys.exit(1)

enc_file = sys.argv[1]
aes_key_file = sys.argv[2]
output_file = sys.argv[3]

with open(aes_key_file, 'rb') as f:
    aes_key = f.read()

with open(enc_file, 'rb') as fin:
    iv = fin.read(16)
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    enc_data = fin.read()
    data = unpad(cipher_aes.decrypt(enc_data), AES.block_size)

with open(output_file, 'wb') as fout:
    fout.write(data)
print(f'文件已解密: {output_file} / File decrypted: {output_file}') 