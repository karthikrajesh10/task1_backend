from datetime import datetime
from tts_stt_backend.backend.tts_service import text_to_speech
from tts_stt_backend.backend.translation_service import translate_to_english


def process_chat(user_text: str, chat_id: int, message_index: int):
    #English translation
    english_text = translate_to_english(user_text)

    #Audio
    audio_file = text_to_speech(
        english_text,
        f"chat{chat_id}_{message_index}"
    )

    return {
        "role": "assistant",
        "original_text": user_text,
        "content": english_text,
        "audio": audio_file,
        "time": datetime.now().strftime("%H:%M")
    }
