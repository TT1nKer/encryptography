from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA

# 加载公钥 / Load public key
with open('public.pem', 'rb') as f:
    public_key = RSA.import_key(f.read())

# 生成AES密钥 / Generate AES key
aes_key = get_random_bytes(32)  # 256位 / 256 bits

# 用RSA公钥加密AES密钥 / Encrypt AES key with RSA public key
cipher_rsa = PKCS1_OAEP.new(public_key)
enc_aes_key = cipher_rsa.encrypt(aes_key)

# 保存加密后的AES密钥 / Save encrypted AES key
with open('encrypted_aes_key.bin', 'wb') as f:
    f.write(enc_aes_key)
# 保存原始AES密钥（仅用于学习，实际应用请勿保存明文密钥）
# Save raw AES key (for learning only, do NOT save plaintext key in real use)
with open('aes_key.bin', 'wb') as f:
    f.write(aes_key)
print('AES密钥已生成并加密: encrypted_aes_key.bin / AES key generated and encrypted: encrypted_aes_key.bin') 