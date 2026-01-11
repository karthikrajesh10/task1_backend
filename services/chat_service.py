# # from services.stt_service import speech_to_text
# # from services.tts_service import text_to_speech

# # def process_text_message(text: str) -> dict:
# #     audio_url = text_to_speech(text)

# #     return {
# #         "type": "text",
# #         "text": text,
# #         "audio": audio_url
# #     }

# # def process_voice_message(audio_path: str, language: str) -> dict:
# #     english_text = speech_to_text(audio_path, language)
# #     audio_url = text_to_speech(english_text)

# #     return {
# #         "type": "voice",
# #         "original_language": language,
# #         "english_text": english_text,
# #         "audio": audio_url
# #     }


# from tts_stt_backend.services.stt_service import speech_to_text
# from tts_stt_backend.services.tts_service import text_to_speech

# async def handle_text_message(text: str) -> dict:
#     audio = text_to_speech(text)

#     return {
#         "type": "text",
#         "english_text": text,
#         "audio": audio
#     }

# def handle_voice_message(audio_path: str, language: str) -> dict:
#     original, english = speech_to_text(audio_path, language)
#     audio = text_to_speech(english)

#     return {
#         "type": "voice",
#         "original_text": original,
#         "english_text": english,
#         "audio": audio
#     }
# tts_stt_backend/services/chat_service.py
from tts_stt_backend.services.stt_service import speech_to_text
from tts_stt_backend.services.tts_service import text_to_speech

def handle_text_message(text: str) -> dict:
    audio_url = text_to_speech(text)

    return {
        "type": "text",
        "english_text": text,
        "audio": audio_url
    }

def handle_voice_message(audio_path: str, language: str) -> dict:
    original, english = speech_to_text(audio_path, language)
    audio_url = text_to_speech(english)

    return {
        "type": "voice",
        "original_text": original,
        "english_text": english,
        "audio": audio_url
    }
