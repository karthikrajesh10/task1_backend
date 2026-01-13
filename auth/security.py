# # from passlib.context import CryptContext
# # from datetime import datetime, timedelta
# # import jwt

# # SECRET_KEY = "super-secret-key"
# # ALGORITHM = "HS256"
# # ACCESS_TOKEN_EXPIRE_MINUTES = 60

# # # ✅ Use argon2 instead of bcrypt
# # pwd_context = CryptContext(
# #     schemes=["argon2"],
# #     deprecated="auto"
# # )


# # def hash_password(password: str) -> str:
# #     return pwd_context.hash(password)


# # def verify_password(password: str, hashed_password: str) -> bool:
# #     return pwd_context.verify(password, hashed_password)


# # def create_access_token(username: str) -> str:
# #     payload = {
# #         "sub": username,
# #         "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
# #     }
# #     return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# # def decode_token(token: str) -> str:
# #     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# #     return payload["sub"]


# from datetime import datetime, timedelta
# import jwt
# from passlib.context import CryptContext
# from tts_stt_backend.config.settings import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRE_MINUTES

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(password: str, hashed: str) -> bool:
#     return pwd_context.verify(password, hashed)

# def create_token(username: str) -> str:
#     payload = {
#         "sub": username,
#         "exp": datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
#     }
#     return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

# def decode_token(token: str) -> str:
#     payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
#     return payload["sub"]


from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from tts_stt_backend.config.settings import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

MAX_BCRYPT_BYTES = 72


def _normalize_password(password: str) -> str:
    
    encoded = password.encode("utf-8")
    if len(encoded) > MAX_BCRYPT_BYTES:
        return encoded[:MAX_BCRYPT_BYTES].decode("utf-8", errors="ignore")
    return password


def hash_password(password: str) -> str:
    password = _normalize_password(password)
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    password = _normalize_password(password)
    return pwd_context.verify(password, hashed)


def create_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRE_MINUTES)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def decode_token(token: str) -> str:
    payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return payload["sub"]
