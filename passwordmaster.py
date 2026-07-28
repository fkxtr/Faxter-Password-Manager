import hashlib
import getpass

password = getpass.getpass("Create master password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

with open("master.hash", "w") as file:
    file.write(hashed)

print("Master password created!")
