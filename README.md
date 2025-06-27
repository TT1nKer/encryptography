# Encryptography

## Usage

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Generate RSA key pair:**
   ```
   python generate_keys.py
   ```

3. **Generate and encrypt AES key:**
   ```
   python encrypt_aes_key.py
   ```

4. **Encrypt your EXE file:**
   ```
   python encrypt_exe.py <your_program.exe>
   ```

- The encrypted AES key (`encrypted_aes_key.bin`) simulates the USB dongle content.
- The encrypted EXE (`encrypted_program.bin`) is your protected executable.
- **Note:** The `aes_key.bin` is only for local use and should be deleted after encrypting the EXE.