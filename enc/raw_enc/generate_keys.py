from Crypto.PublicKey import RSA

# 生成RSA密钥对 / Generate RSA key pair
key = RSA.generate(4096)
private_key = key.export_key()
public_key = key.publickey().export_key()

# 保存私钥 / Save private key
with open('private.pem', 'wb') as f:
    f.write(private_key)
# 保存公钥 / Save public key
with open('public.pem', 'wb') as f:
    f.write(public_key)
print('RSA密钥对已生成: private.pem, public.pem / RSA key pair generated: private.pem, public.pem') 