from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import sys
import os

# 用法: python encrypt_exe.py <要加密的文件路径>
# Usage: python encrypt_exe.py <file_to_encrypt>
if len(sys.argv) != 2:
    print('用法: python encrypt_exe.py <要加密的文件路径>')
    print('Usage: python encrypt_exe.py <file_to_encrypt>')
    sys.exit(1)

input_file = sys.argv[1]
if not os.path.isfile(input_file):
    print(f'文件未找到: {input_file} / File not found: {input_file}')
    sys.exit(1)

# 加载AES密钥 / Load AES key
# 注意：实际应用中不应保存明文AES密钥 / Note: Do NOT save plaintext AES key in real use
with open('aes_key.bin', 'rb') as f:
    aes_key = f.read()

# 加密文件 / Encrypt file
with open(input_file, 'rb') as f:
    file_data = f.read()

cipher_aes = AES.new(aes_key, AES.MODE_CBC)
iv = cipher_aes.iv
enc_data = cipher_aes.encrypt(pad(file_data, AES.block_size))

# 保存加密后的文件 / Save encrypted file
with open('encrypted_program.bin', 'wb') as f:
    f.write(iv + enc_data)
print('文件已加密: encrypted_program.bin / File encrypted: encrypted_program.bin') 