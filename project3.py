# ---------------------------
# ENCODING / DECODING
# ---------------------------

def encode(text):
    result = ""
    for char in text:
        result += chr(ord(char) + 3)
    return result


def decode(text):
    result = ""
    for char in text:
        result += chr(ord(char) - 3)
    return result


# ---------------------------
# PASSWORD CLASS
# ---------------------------

class Password:
    def __init__(self, account, username, password, encoded=False):
        self.account = account
        self.username = username

        if encoded:
            self.password = password            # already encoded
        else:
            self.password = encode(password)    # encode raw password

    def save(self):
        with open("password.txt", "a") as file:
            file.write(f"{self.account};{self.username};{self.password}\n")

    def show(self):
        print("\n-------------------")
        print(f"Account: {self.account}")
        print(f"Username: {self.username}")
        print(f"Password (decoded): {decode(self.password)}")
        print("-------------------")


# ---------------------------
# LOAD PASSWORDS
# ---------------------------

def load_passwords():
    passwords = []
    try:
        with open("password.txt", "r") as file:
            for line in file:
                if line.strip() == "":
                    continue

                try:
                    account, username, encoded_pass = line.strip().split(";")
                    p = Password(account, username, encoded_pass, encoded=True)
                    passwords.append(p)
                except ValueError:
                    print("Skipping corrupted line:", line.strip())

    except FileNotFoundError:
        print("No password data yet.")

    return passwords


# ---------------------------
# MENU + MAIN LOOP
# ---------------------------

def show_menu():
    print("\n----- Password Manager -----")
    print("1: Add Password")
    print("2: Show All Passwords")
    print("3: Search Password")
    print("4: Exit\n")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            account = input("Enter account: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            p = Password(account, username, password)
            p.save()

            print("Password saved!\n")

        elif choice == "2":
            passwords = load_passwords()
            if not passwords:
                print("No passwords found.\n")
            else:
                for p in passwords:
                    p.show()

        elif choice == "3":
            search = input("Enter keyword to search: ").lower()
            passwords = load_passwords()

            found = False
            for p in passwords:
                if search in p.account.lower():
                    p.show()
                    found = True

            if not found:
                print("No matching passwords.\n")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()
