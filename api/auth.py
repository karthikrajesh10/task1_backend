# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel

# from auth.security import hash_password, verify_password, create_access_token
# from TextToSpeech.tts_stt_backend.auth.users import create_user, get_user

# router = APIRouter(prefix="/auth", tags=["Auth"])


# class SignupRequest(BaseModel):
#     username: str
#     password: str


# class LoginRequest(BaseModel):
#     username: str
#     password: str


# @router.post("/signup")
# def signup(data: SignupRequest):
#     if get_user(data.username):
#         raise HTTPException(status_code=400, detail="User already exists")

#     hashed = hash_password(data.password)
#     create_user(data.username, hashed)
#     return {"message": "User created successfully"}


# @router.post("/login")
# def login(data: LoginRequest):
#     stored_password = get_user(data.username)

#     if not stored_password or not verify_password(data.password, stored_password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")

#     token = create_access_token(data.username)
#     return {"access_token": token}


from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from tts_stt_backend.auth.users import create_user, authenticate_user
from tts_stt_backend.auth.security import create_token


router = APIRouter(prefix="/auth", tags=["Auth"])

class AuthRequest(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(data: AuthRequest):
    try:
        create_user(data.username, data.password)
        return {"message": "Signup successful"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(data: AuthRequest):
    if not authenticate_user(data.username, data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(data.username)
    return {"access_token": token}
