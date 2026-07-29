# Faxter Password Manager

A simple terminal-based password manager written in Python.

Faxter Password Manager allows you to generate strong passwords, encrypt them using Fernet, and store them securely inside an encrypted vault protected by a master password. The project was built as a learning exercise to practice cryptography, file handling, hashing, and terminal application development with Python.

---

## Features

- Generate cryptographically secure passwords.
- Encrypt every stored password using Fernet.
- Master password authentication.
- Search saved passwords.
- Delete stored passwords.
- Simple terminal interface.
- Customizable terminal colors.

---

## Requirements

- Python 3.10 or newer

Install the required dependencies:

```bash
pip install cryptography colorama
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/fkxtr/Faxter-Password-Manager.git
```

Enter the project folder:

```bash
cd Faxter-Password-Manager
```

Before running the password manager, execute the setup scripts:

```bash
python keymaster.py
python passwordmaster.py
```

These scripts will:

- Generate the encryption key (`secret.key`)
- Create and hash your master password (`master.hash`)

Once the setup is complete, launch the application:

```bash
python main.py
```

---

## Project Structure

```text
Faxter-Password-Manager/
│
├── main.py
├── keymaster.py
├── passwordmaster.py
├── secret.key
├── master.hash
├── passwords/
│   └── vault.enc
└── README.md
```

---

## How It Works

### Initial Setup

Before using the application, you must run:

```bash
python keymaster.py
python passwordmaster.py
```

`keymaster.py` generates the Fernet encryption key used to encrypt and decrypt your password vault.

`passwordmaster.py` asks you to create a master password and stores only its SHA-256 hash inside `master.hash`.

This setup only needs to be completed once.

---

### Running the Application

Start the password manager with:

```bash
python main.py
```

After entering the correct master password, you can use the application's menu to:

- Generate secure passwords
- Save new passwords
- View saved entries
- Search for passwords
- Delete existing entries

---

## Security

The project uses several security mechanisms:

- Fernet encryption from the `cryptography` library.
- SHA-256 hashing for the master password.
- Secure random password generation using Python's `secrets` module.
- Passwords are encrypted before being written to disk.
- The master password is never stored in plain text.

Encrypted passwords are stored in:

```text
passwords/vault.enc
```

The encryption key is stored in:

```text
secret.key
```

The master password hash is stored in:

```text
master.hash
```

---

## Technologies Used

- Python
- Cryptography (Fernet)
- Colorama
- Hashlib
- Secrets
- Getpass

---

## Notes

- Run the program from the project directory.
- Do not delete `secret.key`, `master.hash`, or the `passwords` folder after creating them.
- Losing `secret.key` means the encrypted vault can no longer be decrypted.
- This project is intended for educational purposes and to demonstrate encryption, hashing, and secure password storage in Python.

---

## License

This project is released under the MIT License.
