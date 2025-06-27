from Crypto.PublicKey import RSA
import sys

# 用法: python load_private_key.py private.pem
# Usage: python load_private_key.py private.pem
if len(sys.argv) != 2:
    print('用法: python load_private_key.py private.pem')
    print('Usage: python load_private_key.py private.pem')
    sys.exit(1)

privkey_path = sys.argv[1]
with open(privkey_path, 'rb') as f:
    private_key = RSA.import_key(f.read())

print('私钥已加载 / Private key loaded')
print(private_key.export_key().decode()) 