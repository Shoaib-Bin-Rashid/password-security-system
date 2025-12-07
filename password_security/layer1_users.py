from layer0_crypto import validate_password_strength, verify_hash, make_stored_password

users = {}

class UserError(Exception):
    pass

def register_user(username: str, password: str):
    if username in users:
        raise UserError("User already exists")
    validate_password_strength(password)
    rec = make_stored_password(password)
    users[username] = {"password": rec, "locked": False, "login_attempts": 0}
    return True

def login_user(username: str, password: str):
    if username not in users:
        raise UserError("User not found")
    user = users[username]
    if user["locked"]:
        raise UserError("Account locked")
    if not verify_hash(password, user["password"]["salt"], user["password"]["hash"], user["password"]["iterations"]):
        user["login_attempts"] += 1
        raise UserError("Invalid credentials")
    user["login_attempts"] = 0
    return True

def logout_user(username: str):
    if username not in users:
        raise UserError("User not found")
    return True

def change_password(username: str, current_password: str, new_password: str):
    if username not in users:
        raise UserError("User not found")
    login_user(username, current_password)
    validate_password_strength(new_password)
    users[username]["password"] = make_stored_password(new_password)
    return True

def lock_account(username: str):
    if username not in users:
        raise UserError("User not found")
    users[username]["locked"] = True

def unlock_account(username: str):
    if username not in users:
        raise UserError("User not found")
    users[username]["locked"] = False
    users[username]["login_attempts"] = 0

def reset_password(username: str, new_password: str):
    if username not in users:
        raise UserError("User not found")
    validate_password_strength(new_password)
    users[username]["password"] = make_stored_password(new_password)
    users[username]["login_attempts"] = 0
    users[username]["locked"] = False

def is_locked(username: str) -> bool:
    if username not in users:
        raise UserError("User not found")
    return users[username]["locked"]