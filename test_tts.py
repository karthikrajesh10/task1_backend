import os
import asyncio
from tts_stt_backend.services.tts_service import text_to_speech

async def test_tts():
    text = "Hello, this is a text to speech unit test."

    audio_url = await text_to_speech(text)

    print("Generated audio URL:", audio_url)

    # Convert URL → local path
    audio_path = audio_url.replace("/audio/", "tts_stt_backend/output/audio/")

    if os.path.exists(audio_path):
        print("✅ TTS test passed. Audio file created:", audio_path)
    else:
        print("❌ TTS test failed. File not found.")

if __name__ == "__main__":
    asyncio.run(test_tts())
