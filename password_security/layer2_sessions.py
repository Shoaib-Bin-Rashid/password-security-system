import secrets
import time
from layer1_users import users, UserError

sessions = {}

def generate_token(username: str, ttl_seconds: int = 3600) -> str:
    if username not in users:
        raise UserError("User not found")
    token = secrets.token_urlsafe(32)
    sessions[token] = {"username": username, "expires_at": time.time() + ttl_seconds}
    return token

def validate_token(token: str) -> bool:
    if token not in sessions:
        return False
    info = sessions[token]
    if time.time() > info["expires_at"]:
        del sessions[token]
        return False
    return True

def revoke_token(token: str):
    sessions.pop(token, None)

def get_username_from_token(token: str):
    if not validate_token(token):
        raise UserError("Invalid or expired token")
    return sessions[token]["username"]

def refresh_token(token: str, ttl_seconds: int = 3600):
    if token not in sessions:
        raise UserError("Token not found")
    sessions[token]["expires_at"] = time.time() + ttl_seconds
    return True