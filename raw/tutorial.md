# Tutorial: Using the `raw` Folder Scripts

The `raw` folder contains the original, step-by-step scripts used to encrypt an executable with asymmetric (RSA) and symmetric (AES) cryptography. These scripts are provided for learning and experimentation.

## Contents of `raw/`
- `generate_keys.py`: Generates an RSA key pair (`private.pem`, `public.pem`).
- `encrypt_aes_key.py`: Generates a random AES key, encrypts it with the RSA public key, and saves both the encrypted AES key and the raw AES key.
- `encrypt_exe.py`: Encrypts a given EXE file using the AES key.

---

## How to Use the Scripts

### 1. Install Dependencies
Make sure you have Python and the required packages installed:
```bash
pip install -r requirements.txt
```

### 2. Generate RSA Key Pair
Run this script to create `private.pem` and `public.pem`:
```bash
python raw/generate_keys.py
```

### 3. Generate and Encrypt AES Key
This script will create a random AES key, encrypt it with the public RSA key, and save both the encrypted and raw AES key:
```bash
python raw/encrypt_aes_key.py
```
- `encrypted_aes_key.bin`: The AES key encrypted with RSA (simulates what would be stored on a USB dongle).
- `aes_key.bin`: The raw AES key (used for the next step, should be deleted after use).

### 4. Encrypt an EXE File
Encrypt your executable using the AES key:
```bash
python raw/encrypt_exe.py <path_to_your_exe>
```
- This will produce `encrypted_program.bin`.

---

## Learning Tips
- Study each script to understand how cryptographic keys are generated and used.
- Try modifying the scripts (e.g., change key sizes, use different files) to see how the process works.
- Remember: In a real system, the private key should be kept secure and never distributed.

---

For a fully automated workflow, use the main `package_exe.py` script in the project root. The `raw` folder is for step-by-step learning and experimentation. 