# 🔒 Encryptography 加密/解密工具 / Encryptography Toolkit

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)



---

## 📖 目录 / Table of Contents
- [🔒 Encryptography 加密/解密工具 / Encryptography Toolkit](#-encryptography-加密解密工具--encryptography-toolkit)
  - [📖 目录 / Table of Contents](#-目录--table-of-contents)
  - [简介 / Introduction](#简介--introduction)
  - [安装依赖 / Install Dependencies](#安装依赖--install-dependencies)
  - [加密工具 enc/enc.py, enc/enc\_gui.py / Encryption Tools](#加密工具-encencpy-encenc_guipy--encryption-tools)
    - [命令行加密工具 / Command-line Encryption Tool](#命令行加密工具--command-line-encryption-tool)
      - [示例 / Example](#示例--example)
    - [图形界面加密工具 / GUI Encryption Tool](#图形界面加密工具--gui-encryption-tool)
    - [功能说明 / Features](#功能说明--features)
  - [解密工具 dec/dec.py, dec/dec\_gui.py / Decryption Tools](#解密工具-decdecpy-decdec_guipy--decryption-tools)
    - [命令行解密工具 / Command-line Decryption Tool](#命令行解密工具--command-line-decryption-tool)
      - [示例 / Example](#示例--example-1)
    - [图形界面解密工具 / GUI Decryption Tool](#图形界面解密工具--gui-decryption-tool)
    - [功能说明 / Features](#功能说明--features-1)
  - [原始学习脚本 enc/raw\_enc, dec/raw\_dec / Raw Learning Scripts](#原始学习脚本-encraw_enc-decraw_dec--raw-learning-scripts)
  - [输出文件 / Output Files](#输出文件--output-files)
  - [安全特性 / Security Features](#安全特性--security-features)

---

## 简介 / Introduction

本项目提供加密和解密工具：
- `enc/enc.py`、`enc/enc_gui.py`：加密工具（命令行和图形界面）
- `dec/dec.py`、`dec/dec_gui.py`：解密工具（命令行和图形界面）

This project provides encryption and decryption tools:
- `enc/enc.py`, `enc/enc_gui.py`: Encryption tools (command-line and GUI)
- `dec/dec.py`, `dec/dec_gui.py`: Decryption tools (command-line and GUI)

---

## 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 加密工具 enc/enc.py, enc/enc_gui.py / Encryption Tools

### 命令行加密工具 / Command-line Encryption Tool
```bash
python enc/enc.py --file <要加密的文件路径/file_to_encrypt> \
                  --enc_dir <加密文件保存目录/encrypted_files_dir> \
                  --privkey_dir <私钥保存目录/private_key_dir>
```
- 如果未提供参数，程序会提示你输入路径。
- If you do not provide arguments, the program will prompt you to enter the paths interactively.

#### 示例 / Example
```bash
python enc/enc.py --file myapp.exe --enc_dir ./encrypted --privkey_dir ./key
```

### 图形界面加密工具 / GUI Encryption Tool
```bash
python enc/enc_gui.py
```
- 选择要加密的文件。
- 选择加密文件保存目录。
- 选择私钥保存目录。
- 点击"Package File"按钮。

- Select the file to encrypt.
- Select the directory to save encrypted files.
- Select the directory to save the private key.
- Click the "Package File" button.

### 功能说明 / Features
- 只保存私钥（private.pem），不保存公钥。
- AES密钥仅在内存中存在，绝不会明文保存。
- 只保存RSA加密后的AES密钥。
- Only private.pem is saved, public.pem is not.
- The AES key exists only in memory and is never saved in plaintext.
- Only the RSA-encrypted AES key is saved.

---

## 解密工具 dec/dec.py, dec/dec_gui.py / Decryption Tools

### 命令行解密工具 / Command-line Decryption Tool
```bash
python dec/dec.py --enc_file <encrypted_program.bin> \
                  --enc_aes_key <encrypted_aes_key.bin> \
                  --privkey <private.pem> \
                  --output <output_file>
```

#### 示例 / Example
```bash
python dec/dec.py --enc_file ./encrypted/encrypted_program.bin --enc_aes_key ./encrypted/encrypted_aes_key.bin --privkey ./key/private.pem --output ./decrypted_output
```

### 图形界面解密工具 / GUI Decryption Tool
```bash
python dec/dec_gui.py
```
- 选择加密文件、加密AES密钥、私钥和输出文件。
- Select the encrypted file, encrypted AES key, private key, and output file.
- 点击"Decrypt File"按钮。
- Click the "Decrypt File" button.

### 功能说明 / Features
- 只需私钥（private.pem）即可解密。
- AES密钥仅在内存中存在，绝不会明文保存。
- Only private.pem is needed for decryption.
- The AES key exists only in memory and is never saved in plaintext.

---

## 原始学习脚本 enc/raw_enc, dec/raw_dec / Raw Learning Scripts

- `enc/raw_enc`：逐步学习加密流程的原始脚本
- `dec/raw_dec`：逐步学习解密流程的原始脚本

- `enc/raw_enc`: Step-by-step learning scripts for encryption
- `dec/raw_dec`: Step-by-step learning scripts for decryption

每个文件夹下有详细的README和注释，适合学习和实验。
Each folder contains a detailed README and comments for learning and experimentation.

---

## 输出文件 / Output Files
- `private.pem`：RSA私钥 / RSA private key
- `encrypted_aes_key.bin`：RSA加密的AES密钥 / AES key encrypted with RSA
- `encrypted_program.bin`：加密后的文件 / Encrypted file

---

## 安全特性 / Security Features
- 只保存私钥（private.pem），不保存公钥。
- AES密钥仅在内存中存在，绝不会明文保存。
- 只保存RSA加密后的AES密钥。
- Only private.pem is saved, public.pem is not.
- The AES key exists only in memory and is never saved in plaintext.
- Only the RSA-encrypted AES key is saved.

---

如有问题请联系开发者。
If you have any questions, please contact the developer.

Copyright (c) 2024 Your Name

This software is free for personal, educational, or non-commercial use.
For commercial or business use, a paid license is required.
Contact [hostsjim22@gmail.com]TT1nker for commercial licensing.

THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND...