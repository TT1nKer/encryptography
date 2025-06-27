# raw_dec 文件夹说明 / About the raw_dec Folder

本文件夹包含用于学习和实验的原始解密脚本，每个脚本实现了解密流程的一个步骤。

This folder contains the original scripts for step-by-step learning and experimentation. Each script implements one step of the decryption process.

---

## 脚本列表 / Script List

- `load_private_key.py`：加载RSA私钥
- `decrypt_aes_key.py`：用私钥解密AES密钥
- `decrypt_file.py`：用AES密钥解密加密文件

- `load_private_key.py`: Load RSA private key
- `decrypt_aes_key.py`: Decrypt AES key with the private key
- `decrypt_file.py`: Decrypt the encrypted file with the AES key

---

## 使用方法 / How to Use

1. 安装依赖 / Install dependencies:
   ```bash
   pip install -r ../../requirements.txt
   ```
2. 加载私钥 / Load private key:
   ```bash
   python load_private_key.py private.pem
   ```
3. 解密AES密钥 / Decrypt AES key:
   ```bash
   python decrypt_aes_key.py encrypted_aes_key.bin private.pem
   ```
4. 解密文件 / Decrypt file:
   ```bash
   python decrypt_file.py encrypted_program.bin <decrypted_aes_key.bin> output_file
   ```

---

## 学习建议 / Learning Tips
- 逐步运行每个脚本，理解每一步的作用。
- 可以尝试修改脚本参数或解密不同文件。
- 这些脚本仅用于学习，实际应用请使用主目录下的dec.py或dec_gui.py。

- Run each script step by step to understand the process.
- Try modifying parameters or decrypting different files.
- These scripts are for learning only; for real use, use `dec.py` or `dec_gui.py` in the main directory. 