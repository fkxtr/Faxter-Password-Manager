# Faxter Password Manager

A simple terminal-based password manager written in Python.

This project allows you to generate strong passwords, encrypt them using Fernet, and store them securely inside an encrypted vault protected by a master password.

## Features

- Generate secure random passwords.
- Store passwords in an encrypted vault.
- Password encryption using Fernet (AES-based symmetric encryption).
- Master password authentication.
- Search stored passwords.
- Delete saved passwords.
- Customizable terminal theme and menu colors.

---

## Requirements

- Python 3.10 or newer

Install the required dependency:

```bash
pip install cryptography colorama
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Faxter-Password-Manager.git
```

Enter the project folder:

```bash
cd Faxter-Password-Manager
```

Run the program:

```bash
python main.py
```

Replace `main.py` with the actual filename if your script has a different name.

---

## Important

The program must be executed from the project's directory.

Example:

```text
C:
└── Users
    └── YourUser
        └── Desktop
            └── Faxter-Password-Manager
                ├── main.py
                ├── secret.key
                ├── master.hash
                └── passwords
```

Open a terminal inside this folder or navigate to it using:

```bash
cd path/to/Faxter-Password-Manager
```

Running the script from another directory may prevent it from locating the encryption key and password vault.

---

## First Launch

When running the application for the first time:

- A new Fernet encryption key (`secret.key`) is generated.
- You will be prompted to create a master password.
- The SHA-256 hash of the master password is stored in `master.hash`.
- An encrypted password vault will be created automatically when the first password is saved.

---

## How It Works

### Password Generation

The application generates random passwords using Python's `secrets` module together with:

- Uppercase letters
- Lowercase letters
- Numbers
- Symbols

This provides cryptographically secure random passwords.

### Encryption

Every password is encrypted before being stored.

The application uses:

- Fernet encryption from the `cryptography` library
- A unique encryption key stored in `secret.key`

The encrypted passwords are saved inside:

```text
passwords/vault.enc
```

The vault does not contain readable text. Every entry is encrypted before being written to disk.

### Master Password

The master password is never stored in plain text.

Instead:

1. The password is hashed using SHA-256.
2. Only the resulting hash is saved in `master.hash`.
3. Each time the Password Vault is opened, the entered password is hashed again and compared with the stored hash.

If the hashes match, access to the vault is granted.

---

## Project Structure

```text
Faxter-Password-Manager/
│
├── main.py
├── secret.key
├── master.hash
├── passwords/
│   └── vault.enc
└── README.md
```

---

## Files

### `secret.key`

Stores the Fernet encryption key used to encrypt and decrypt the password vault.

### `master.hash`

Contains the SHA-256 hash of the master password.

### `vault.enc`

Contains every saved password in encrypted form.

---

## Security Notes

- Passwords are never stored in plain text.
- The master password itself is never stored.
- All stored entries are encrypted before being written to disk.
- Random passwords are generated using Python's `secrets` module.

This project is intended for educational purposes and as a demonstration of Python file encryption, hashing, and terminal application development.

---

## Technologies Used

- Python
- Cryptography (Fernet)
- Colorama
- Hashlib
- Getpass
- Secrets

---

## License

This project is open source and available under the MIT License.
