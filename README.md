# 🔒 Encryptography 加密工具 / Encryptography Toolkit

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/) [![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **双语/Bilingual:** [中文说明在下方 | English below]

---

## 📖 目录 / Table of Contents
- [🔒 Encryptography 加密工具 / Encryptography Toolkit](#-encryptography-加密工具--encryptography-toolkit)
  - [📖 目录 / Table of Contents](#-目录--table-of-contents)
  - [简介 / Introduction](#简介--introduction)
  - [安装依赖 / Install Dependencies](#安装依赖--install-dependencies)
  - [命令行加密工具 enc.py / Command-line Tool](#命令行加密工具-encpy--command-line-tool)
    - [用法 / Usage](#用法--usage)
      - [示例 / Example](#示例--example)
  - [图形界面加密工具 enc\_gui.py / GUI Tool](#图形界面加密工具-enc_guipy--gui-tool)
    - [用法 / Usage](#用法--usage-1)
    - [功能说明 / Features](#功能说明--features)
  - [输出文件 / Output Files](#输出文件--output-files)
  - [安全特性 / Security Features](#安全特性--security-features)

---

## 简介 / Introduction

本项目提供两种加密工具：
- `enc.py`：命令行加密工具
- `enc_gui.py`：图形界面加密工具

This project provides two encryption tools:
- `enc.py`: Command-line encryption tool
- `enc_gui.py`: Graphical user interface (GUI) encryption tool

---

## 安装依赖 / Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 命令行加密工具 enc.py / Command-line Tool

### 用法 / Usage
```bash
python enc.py --file <要加密的文件路径/file_to_encrypt> \
              --enc_dir <加密文件和公钥保存目录/encrypted_files_and_public_key_dir> \
              --privkey_dir <私钥保存目录/private_key_dir>
```
- 如果未提供参数，程序会提示你输入路径。
- If you do not provide arguments, the program will prompt you to enter the paths interactively.

#### 示例 / Example
```bash
python enc.py --file myapp.exe --enc_dir ./encrypted --privkey_dir ./key
```

- `private.pem` 会保存在私钥目录。
- `public.pem`、`encrypted_aes_key.bin`、`encrypted_program.bin` 会保存在加密文件目录。
- `private.pem` will be saved in the private key directory.
- `public.pem`, `encrypted_aes_key.bin`, and `encrypted_program.bin` will be saved in the encrypted files directory.

---

## 图形界面加密工具 enc_gui.py / GUI Tool

### 用法 / Usage
```bash
python enc_gui.py
```

- 选择要加密的文件。
- 选择加密文件和公钥保存目录。
- 选择私钥保存目录。
- 点击"Package File"按钮。

- Select the file to encrypt.
- Select the directory to save encrypted files and public key.
- Select the directory to save the private key.
- Click the "Package File" button.

### 功能说明 / Features
- AES密钥仅在内存中存在，绝不会明文保存。
- 只保存RSA加密后的AES密钥。
- The AES key exists only in memory and is never saved in plaintext.
- Only the RSA-encrypted AES key is saved.

---

## 输出文件 / Output Files
- `private.pem`：RSA私钥 / RSA private key
- `public.pem`：RSA公钥 / RSA public key
- `encrypted_aes_key.bin`：RSA加密的AES密钥 / AES key encrypted with RSA
- `encrypted_program.bin`：加密后的文件 / Encrypted file

---

## 安全特性 / Security Features
- AES密钥仅在内存中存在，绝不会明文保存。
- 只保存RSA加密后的AES密钥。
- The AES key exists only in memory and is never saved in plaintext.
- Only the RSA-encrypted AES key is saved.

---

如有问题请联系开发者。
If you have any questions, please contact the developer.