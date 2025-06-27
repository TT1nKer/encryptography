from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import sys
import os

# Usage: python encrypt_exe.py <input_exe>
if len(sys.argv) != 2:
    print('Usage: python encrypt_exe.py <input_exe>')
    sys.exit(1)

input_exe = sys.argv[1]
if not os.path.isfile(input_exe):
    print(f'File not found: {input_exe}')
    sys.exit(1)

# Load AES key
aes_key_path = 'aes_key.bin'
if not os.path.isfile(aes_key_path):
    print('AES key file not found. Run encrypt_aes_key.py first.')
    sys.exit(1)
with open(aes_key_path, 'rb') as f:
    aes_key = f.read()

# Encrypt EXE file
with open(input_exe, 'rb') as f:
    exe_data = f.read()

cipher_aes = AES.new(aes_key, AES.MODE_CBC)
iv = cipher_aes.iv
enc_exe = cipher_aes.encrypt(pad(exe_data, AES.block_size))

with open('encrypted_program.bin', 'wb') as f:
    f.write(iv + enc_exe)
print('EXE encrypted: encrypted_program.bin') 