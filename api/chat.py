# # import os
# # import uuid
# # from fastapi import APIRouter, UploadFile, File, Form, Depends, Header, HTTPException
# # from tts_stt_backend.services.chat_service import handle_text_message, handle_voice_message
# # from tts_stt_backend.auth.security import decode_token

# # router = APIRouter(prefix="/chat", tags=["Chat"])

# # def get_user(authorization: str = Header(...)):
# #     try:
# #         token = authorization.replace("Bearer ", "")
# #         return decode_token(token)
# #     except Exception:
# #         raise HTTPException(status_code=401, detail="Invalid token")

# # @router.post("")
# # async def chat(
# #     text: str | None = Form(None),
# #     language: str | None = Form("en"),
# #     audio: UploadFile | None = File(None),
# #     user: str = Depends(get_user)
# # ):
# #     if audio:
# #         os.makedirs("temp", exist_ok=True)
# #         temp_path = f"temp/{uuid.uuid4()}.wav"

# #         with open(temp_path, "wb") as f:
# #             f.write(await audio.read())

# #         return await handle_voice_message(temp_path, language)

# #     if text:
# #         return  await handle_text_message(text)

# #     return {"error": "No input provided"}

# # tts_stt_backend/api/chat.py

# #latest 
# import os
# import uuid
# from fastapi import APIRouter, UploadFile, File, Form, Depends, Header, HTTPException
# from tts_stt_backend.services.chat_service import (
#     handle_text_message,
#     handle_voice_message
# )
# from tts_stt_backend.auth.security import decode_token

# router = APIRouter(prefix="/chat", tags=["Chat"])

# def get_user(authorization: str = Header(...)):
#     try:
#         token = authorization.replace("Bearer ", "")
#         return decode_token(token)
#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid token")

# @router.post("")
# async def chat(
#     text: str | None = Form(None),
#     language: str = Form("en"),
#     audio: UploadFile | None = File(None),
#     user: str = Depends(get_user)
# ):
#     if audio:
#         os.makedirs("temp", exist_ok=True)
#         temp_path = f"temp/{uuid.uuid4()}.wav"

#         with open(temp_path, "wb") as f:
#             f.write(await audio.read())

#         return handle_voice_message(temp_path, language)

#     if text:
#         return handle_text_message(text)

#     return {"error": "No input provided"}


import os
import uuid
from fastapi import APIRouter, UploadFile, File, Form, Depends, Header, HTTPException
from tts_stt_backend.services.chat_service import (
    handle_text_message,
    handle_voice_message
)
from tts_stt_backend.auth.security import decode_token

router = APIRouter(prefix="/chat", tags=["Chat"])

def get_user(authorization: str = Header(...)):
    try:
        token = authorization.replace("Bearer ", "")
        return decode_token(token)
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("")
async def chat(
    text: str | None = Form(None),
    language: str = Form("en"),
    audio: UploadFile | None = File(None),
    user: str = Depends(get_user)
):
    if audio:
        os.makedirs("temp", exist_ok=True)
        temp_path = f"temp/{uuid.uuid4()}.wav"

        with open(temp_path, "wb") as f:
            f.write(await audio.read())

        return await handle_voice_message(temp_path, language)

    if text:
        return await handle_text_message(text)

    raise HTTPException(status_code=400, detail="No input provided")
