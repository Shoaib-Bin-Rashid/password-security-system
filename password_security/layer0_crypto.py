import hashlib
import hmac
import secrets
import base64

COMMON_PASSWORDS = {"password", "123456", "qwerty", "letmein", "admin", "welcome"}

def validate_password_strength(password: str, min_len: int = 8) -> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    if len(password) < min_len:
        raise ValueError("Password too short")
    if password.lower() in COMMON_PASSWORDS:
        raise ValueError("Password is too common")
    if not any(c.isdigit() for c in password) or not any(c.isalpha() for c in password):
        raise ValueError("Password must contain letters and digits")
    return True

def generate_salt(length: int = 16) -> str:
    if length < 8:
        raise ValueError("Salt length must be >= 8")
    return base64.b64encode(secrets.token_bytes(length)).decode()

def combine_password_salt(password: str, salt: str) -> bytes:
    if not isinstance(password, str) or not isinstance(salt, str):
        raise TypeError("password and salt must be strings")
    return (password + salt).encode()

def hash_password(password: str, salt: str, iterations: int = 100000) -> str:
    if iterations <= 0:
        raise ValueError("Iterations must be positive")
    combine_password_salt(password, salt)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), iterations)
    return base64.b64encode(dk).decode()

def verify_hash(password: str, salt: str, hashed: str, iterations: int = 100000) -> bool:
    if not isinstance(hashed, str):
        raise TypeError("hashed must be a string")
    expected = hash_password(password, salt, iterations)
    return hmac.compare_digest(expected, hashed)

def check_common_passwords(password: str) -> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    return password.lower() in COMMON_PASSWORDS

def make_stored_password(password: str, salt: str = None, iterations: int = 100000) -> dict:
    if salt is None:
        salt = generate_salt()
    validate_password_strength(password)
    hashed = hash_password(password, salt, iterations)
    return {"salt": salt, "hash": hashed, "iterations": iterations}