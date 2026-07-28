import os
import hashlib
import getpass
from cryptography.fernet import Fernet, InvalidToken
import secrets
import string
import time
from colorama import init, Fore, Back, Style

init(autoreset=True)  

theme_map = {
    "Dark": Back.BLACK,
    "Light": Back.WHITE,
}


BANNER = r"""
 _____          _              ____                                     _ 
|  ___|_ ___  _| |_ ___ _ __  |  _ \ __ _ ___ _____      _____  _ __ __| |
| |_ / _` \ \/ / __/ _ \ '__| | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` |
|  _| (_| |>  <| ||  __/ |    |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| |
|_|  \__,_/_/\_\\__\___|_|    |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|
|  \/  | __ _ _ __   __ _  __ _  ___ _ __                                 
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|                                
| |  | | (_| | | | | (_| | (_| |  __/ |                                   
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|                                   
                          |___/                                                                                     
"""

PASSOWRD_VAULT_MENU = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                    P A S S W O R D   V A U L T               ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  [1] View Passwords                                          ║
║  [2] Search Password                                         ║
║  [3] Delete Password                                         ║
║                                                              ║
║  [0] Back                                                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝"""

MAIN_MENU = r"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║               F A X T E R   P A S S W O R D                  ║
║                       M A N A G E R                          ║
║                                                              ║
║                         main menu                            ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  [1] Password Generator                                      ║
║  [2] Settings                                                ║
║  [3] Password Vault                                          ║
║  [0] Exit                                                    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

colors = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA,
]
color_map = {
    "Red": Fore.RED,
    "Yellow": Fore.YELLOW,
    "Green": Fore.GREEN,
    "Cyan": Fore.CYAN,
    "Blue": Fore.BLUE,
    "Magenta": Fore.MAGENTA,
    "White": Fore.WHITE,
}


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def setup_master_password():
    """
    FIX: antes no existía ningún flujo para crear secret.key y master.hash.
    Si estos archivos no existen, el programa se caía con FileNotFoundError
    apenas arrancaba. Ahora, si es la primera vez, se piden y se crean.
    """
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as file:
            file.write(key)

    if not os.path.exists("master.hash"):
        print("No se detectó una contraseña maestra. Vamos a crear una.\n")
        while True:
            password = getpass.getpass("Crea tu contraseña maestra: ")
            confirm = getpass.getpass("Confirma tu contraseña maestra: ")
            if password == confirm and password.strip() != "":
                hashed = hashlib.sha256(password.encode()).hexdigest()
                with open("master.hash", "w") as file:
                    file.write(hashed)
                print("\nContraseña maestra creada correctamente.\n")
                time.sleep(1)
                break
            else:
                print("\nLas contraseñas no coinciden o están vacías. Intenta de nuevo.\n")


def load_key():
    with open("secret.key", "rb") as file:
        return file.read()


def verify_master():
    password = getpass.getpass("Enter master password: ")
    hashed = hashlib.sha256(password.encode()).hexdigest()

    with open("master.hash", "r") as file:
        saved_hash = file.read()

    return hashed == saved_hash



setup_master_password()  
key = load_key()
cipher = Fernet(key)

menu_color = "Cyan"
theme = "Dark"

for _ in range(3):
    for color in colors:
        clear()
        print(color + BANNER)
        time.sleep(0.10)

clear()

while True:

    clear()

    option = input(
        theme_map[theme]
        + color_map[menu_color]
        + MAIN_MENU
        + Style.RESET_ALL
        + "\nSelect an option > "
    )

    # PASSWORD GENERATOR
    if option == "1":
        clear()

        app_name = input("What is this password for? > ").strip()

        if app_name == "":  # FIX: evita guardar un registro sin nombre de servicio
            print("\nEl nombre del servicio no puede estar vacío.")
            input("\nPress Enter to return to the main menu...")
            continue

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(secrets.choice(characters) for _ in range(20))

        print(f"\nYour password for {app_name} is:")
        print(password)

        os.makedirs("passwords", exist_ok=True)

        data = f"Service: {app_name}\nPassword: {password}"
        encrypted = cipher.encrypt(data.encode())

        with open("passwords/vault.enc", "ab") as file:
            file.write(encrypted + b"\n")

        print("\nPassword encrypted and saved successfully!")
        input("\nPress Enter to return to the main menu...")

    
    elif option == "2":
        while True:
            clear()

            print(
                theme_map[theme]
                + color_map[menu_color]
                + f"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║                         S E T T I N G S                      ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Current Theme : {theme:<43}                                 ║
║  Current Color : {menu_color:<42}                            ║
║                                                              ║
║  [1] Theme (Dark / Light)                                    ║
║  [2] Menu Color                                              ║
║                                                              ║
║  [0] Back to Main Menu                                       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""
                + Style.RESET_ALL
            )

            option2 = input("Select an option > ")

            if option2 == "1":
                clear()
                print(
                    theme_map[theme]
                    + color_map[menu_color]
                    + """
╔════════════════════════════╗
║         T H E M E          ║
╠════════════════════════════╣
║                            ║
║ [1] Dark                   ║
║ [2] Light                  ║
║                            ║
║ [0] Back                   ║
║                            ║
╚════════════════════════════╝
"""
                    + Style.RESET_ALL
                )

                theme_option = input("Select an option > ")

                if theme_option == "1":
                    theme = "Dark"
                elif theme_option == "2":
                    theme = "Light"

            elif option2 == "2":
                clear()
                print(
                    theme_map[theme]
                    + color_map[menu_color]
                    + """
╔════════════════════════════╗
║      M E N U  C O L O R    ║
╠════════════════════════════╣
║                            ║
║ [1] Red                    ║
║ [2] Yellow                 ║
║ [3] Green                  ║
║ [4] Cyan                   ║
║ [5] Blue                   ║
║ [6] Magenta                ║
║ [7] White                  ║
║                            ║
║ [0] Back                   ║
║                            ║
╚════════════════════════════╝
"""
                    + Style.RESET_ALL
                )

                color_option = input("Select an option > ")

                colors_dict = {
                    "1": "Red",
                    "2": "Yellow",
                    "3": "Green",
                    "4": "Cyan",
                    "5": "Blue",
                    "6": "Magenta",
                    "7": "White",
                }

                if color_option in colors_dict:
                    menu_color = colors_dict[color_option]

            elif option2 == "0":
                break

    
    elif option == "3":
        clear()

        if not verify_master():
            print("\nWrong master password.")
            input("\nPress Enter...")
            continue

        while True:
            clear()

            print(
                theme_map[theme]
                + color_map[menu_color]
                + PASSOWRD_VAULT_MENU
                + Style.RESET_ALL
            )

            vault_option = input("\nSelect an option > ")

            # VIEW PASSWORDS
            if vault_option == "1":
                clear()

                try:
                    with open("passwords/vault.enc", "rb") as file:
                        for line in file:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                decrypted = cipher.decrypt(line)  # FIX: manejo de token inválido
                                print(decrypted.decode())
                                print("-" * 40)
                            except InvalidToken:
                                print("(Registro corrupto, se omitió una línea)")
                except FileNotFoundError:
                    print("No passwords have been saved yet.")

                input("\nPress Enter to continue...")

            # SEARCH PASSWORD
            elif vault_option == "2":
                clear()

                search = input("Service name > ").lower()
                found = False

                try:
                    with open("passwords/vault.enc", "rb") as file:
                        for line in file:
                            line = line.strip()
                            if not line:
                                continue
                            try:
                                decrypted = cipher.decrypt(line).decode()
                            except InvalidToken:
                                continue

                            if search in decrypted.lower():
                                print(decrypted)
                                print("-" * 40)
                                found = True

                    if not found:
                        print("\nPassword not found.")

                except FileNotFoundError:
                    print("Vault is empty.")

                input("\nPress Enter...")

            # DELETE PASSWORD
            elif vault_option == "3":
                
                clear()

                try:
                    with open("passwords/vault.enc", "rb") as file:
                        lines = [l.strip() for l in file if l.strip()]
                except FileNotFoundError:
                    lines = []

                if not lines:
                    print("Vault is empty.")
                    input("\nPress Enter...")
                    continue

                entries = []
                for line in lines:
                    try:
                        decrypted = cipher.decrypt(line).decode()
                        entries.append((line, decrypted))
                    except InvalidToken:
                        continue

                for i, (_, decrypted) in enumerate(entries, start=1):
                    print(f"[{i}] {decrypted}")
                    print("-" * 40)

                choice = input("\nNumber to delete (0 to cancel) > ")

                if choice.isdigit() and 1 <= int(choice) <= len(entries):
                    index_to_remove = int(choice) - 1
                    remaining = [enc for i, (enc, _) in enumerate(entries) if i != index_to_remove]

                    with open("passwords/vault.enc", "wb") as file:
                        for enc in remaining:
                            file.write(enc + b"\n")

                    print("\nEntry deleted.")
                else:
                    print("\nCancelled.")

                input("\nPress Enter...")

            
            elif vault_option == "0":
                break

    
    elif option == "0":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid option.")
        input("\nPress Enter to continue...")

input("\nPress Enter to close...")
