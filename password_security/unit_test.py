from layer0_pass import *
from layer1_users import *
from layer2_sessions import *

shared_password = None

def layer0_menu():
    global shared_password
    if shared_password is None:
        shared_password = input("Enter password for Layer 0: ")

    print("\n--- Layer 0: Password Tests ---")
    print("1. Validate Password")
    print("2. Generate Salt")
    print("3. Hash Password")
    print("4. Verify Password")
    print("0. Back")

    choice = input("Choose: ")

    if choice == "1":
        try:
            validate_password_strength(shared_password)
            print("Password is strong")
        except Exception as e:
            print("Error:", e)

    elif choice == "2":
        try:
            length = int(input("Salt length: "))
            print("Generated salt:", generate_salt(length))
        except Exception as e:
            print("Error:", e)

    elif choice == "3":
        salt = generate_salt()
        print("Using salt:", salt)
        try:
            h = hash_password(shared_password, salt)
            print("Hash:", h)
        except Exception as e:
            print("Error:", e)

    elif choice == "4":
        salt = generate_salt()
        record = make_stored_password(shared_password, salt)
        test_pwd = input("Enter password to verify: ")
        try:
            if verify_hash(test_pwd, record["salt"], record["hash"], record["iterations"]):
                print("Password matched")
            else:
                print("Password NOT matched")
        except Exception as e:
            print("Error:", e)

def layer1_menu():
    print("\n--- Layer 1: User System ---")
    print("1. Register User")
    print("2. Login User")
    print("3. Change Password")
    print("4. Lock User")
    print("5. Unlock User")
    print("6. Reset Password")
    print("0. Back")

    choice = input("Choose: ")

    try:
        if choice == "1":
            u = input("Username: ")
            register_user(u, shared_password)
            print("User registered")

        elif choice == "2":
            u = input("Username: ")
            login_user(u, shared_password)
            print("Login successful")

        elif choice == "3":
            u = input("Username: ")
            new = input("New password: ")
            change_password(u, shared_password, new)
            print("Password changed")

        elif choice == "4":
            u = input("Username: ")
            lock_account(u)
            print("User locked")

        elif choice == "5":
            u = input("Username: ")
            unlock_account(u)
            print("User unlocked")

        elif choice == "6":
            u = input("Username: ")
            reset_password(u, shared_password)
            print("Password reset")

    except Exception as e:
        print("Error:", e)

def layer2_menu():
    print("\n--- Layer 2: Sessions ---")
    print("1. Generate Token")
    print("2. Validate Token")
    print("3. Revoke Token")
    print("4. Get Username From Token")
    print("5. Refresh Token")
    print("0. Back")

    choice = input("Choose: ")

    try:
        if choice == "1":
            u = input("Username: ")
            t = generate_token(u)
            print("Token:", t)

        elif choice == "2":
            t = input("Token: ")
            print("Valid" if validate_token(t) else "Invalid")

        elif choice == "3":
            t = input("Token: ")
            revoke_token(t)
            print("Token revoked")

        elif choice == "4":
            t = input("Token: ")
            print("Username:", get_username_from_token(t))

        elif choice == "5":
            t = input("Token: ")
            refresh_token(t)
            print("Token refreshed")

    except Exception as e:
        print("Error:", e)

def main_menu():
    while True:
        print("\n===== Password Security Test System =====")
        print("1. Layer 0 - Password")
        print("2. Layer 1 - Users")
        print("3. Layer 2 - Sessions")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            layer0_menu()
        elif choice == "2":
            layer1_menu()
        elif choice == "3":
            layer2_menu()
        elif choice == "0":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main_menu()
