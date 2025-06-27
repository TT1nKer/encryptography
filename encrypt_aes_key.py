from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

# Load public key
with open('public.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# Generate AES key
aes_key = get_random_bytes(32)  # 256 bits

# Encrypt AES key with RSA public key
cipher_rsa = PKCS1_OAEP.new(public_key)
enc_aes_key = cipher_rsa.encrypt(aes_key)

with open('encrypted_aes_key.bin', 'wb') as f:
    f.write(enc_aes_key)
with open('aes_key.bin', 'wb') as f:
    f.write(aes_key)  # For use in EXE encryption (should be deleted after use)
print('AES key generated and encrypted: encrypted_aes_key.bin') 