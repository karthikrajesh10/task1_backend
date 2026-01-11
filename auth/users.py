# # database/users.py

# _users = {}        # username -> hashed_password
# _chat_history = {} # username -> list of chats


# def create_user(username: str, hashed_password: str):
#     _users[username] = hashed_password
#     _chat_history[username] = []


# def get_user(username: str):
#     return _users.get(username)


# def save_chat(username: str, message: dict):
#     _chat_history[username].append(message)


# def get_chat_history(username: str):
#     return _chat_history.get(username, [])



from tts_stt_backend.auth.security import hash_password, verify_password

_users = {}

def create_user(username: str, password: str):
    if username in _users:
        raise ValueError("User already exists")
    _users[username] = hash_password(password)

def authenticate_user(username: str, password: str) -> bool:
    if username not in _users:
        return False
    return verify_password(password, _users[username])
