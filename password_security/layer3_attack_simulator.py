from layer1_users import users, lock_account, UserError

FAILED_THRESHOLD = 3

def record_failed_attempt(username: str):
    if username not in users:
        raise UserError("User not found")
    users[username]["login_attempts"] += 1
    if users[username]["login_attempts"] >= FAILED_THRESHOLD:
        lock_account(username)

def reset_failed_attempts(username: str):
    if username not in users:
        raise UserError("User not found")
    users[username]["login_attempts"] = 0

def detect_bruteforce(username: str) -> bool:
    if username not in users:
        raise UserError("User not found")
    return users[username]["login_attempts"] >= FAILED_THRESHOLD

def simulate_bruteforce(username: str, wrong_password: str, tries: int = 5):
    if username not in users:
        raise UserError("User not found")
    for _ in range(tries):
        try:
            from layer1_users import login_user
            login_user(username, wrong_password)
        except UserError:
            record_failed_attempt(username)
    return detect_bruteforce(username)