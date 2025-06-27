# raw_enc 文件夹说明 / About the raw_enc Folder

本文件夹包含用于学习和实验的原始加密脚本，每个脚本实现了加密流程的一个步骤。

This folder contains the original scripts for step-by-step learning and experimentation. Each script implements one step of the encryption process.

---

## 脚本列表 / Script List

- `generate_keys.py`：生成RSA密钥对（private.pem）
- `encrypt_aes_key.py`：生成AES密钥并用RSA公钥加密，保存加密后的AES密钥
- `encrypt_exe.py`：用AES密钥加密指定文件（如EXE）

- `generate_keys.py`: Generate RSA key pair (`private.pem`)
- `encrypt_aes_key.py`: Generate an AES key, encrypt it with the RSA public key, and save the encrypted AES key
- `encrypt_exe.py`: Encrypt a specified file (e.g., EXE) with the AES key

---

## 使用方法 / How to Use

1. 安装依赖 / Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```
2. 生成RSA密钥对 / Generate RSA key pair:
   ```bash
   python generate_keys.py
   ```
3. 生成并加密AES密钥 / Generate and encrypt AES key:
   ```bash
   python encrypt_aes_key.py
   ```
4. 加密文件 / Encrypt a file:
   ```bash
   python encrypt_exe.py <your_file>
   ```

---

## 学习建议 / Learning Tips
- 逐步运行每个脚本，理解每一步的作用。
- 可以尝试修改脚本参数或加密不同文件。
- 这些脚本仅用于学习，实际应用请使用主目录下的enc.py或enc_gui.py。

- Run each script step by step to understand the process.
- Try modifying parameters or encrypting different files.
- These scripts are for learning only; for real use, use `enc.py` or `enc_gui.py` in the main directory. 