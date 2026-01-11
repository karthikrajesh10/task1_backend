# # import os
# # import uuid
# # from config.settings import TTS_ENGINE, AUDIO_OUTPUT_DIR

# # def text_to_speech(text: str) -> str:
# #     os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

# #     filename = f"{uuid.uuid4()}.mp3"
# #     output_path = os.path.join(AUDIO_OUTPUT_DIR, filename)

# #     TTS_ENGINE.synthesize(text, output_path)

# #     return f"/audio/{filename}"


# # import os
# # import uuid
# # from tts_stt_backend.config.settings import TTS_ENGINE, AUDIO_DIR

# # async def text_to_speech(text: str) -> str:
# #     os.makedirs(AUDIO_DIR, exist_ok=True)

# #     filename = f"{uuid.uuid4()}.mp3"
# #     output_path = os.path.join(AUDIO_DIR, filename)

# #     await TTS_ENGINE.synthesize(text, output_path)



# #     return f"/audio/{filename}"


# # tts_stt_backend/services/tts_service.py
# import os
# import uuid
# import asyncio
# from tts_stt_backend.config.settings import TTS_ENGINE, AUDIO_DIR

# def text_to_speech(text: str) -> str:
#     os.makedirs(AUDIO_DIR, exist_ok=True)

#     filename = f"{uuid.uuid4()}.mp3"
#     output_path = os.path.join(AUDIO_DIR, filename)

#     # Safely run async engine from sync code
#     asyncio.run(TTS_ENGINE.synthesize(text, output_path))

#     return f"/audio/{filename}"


# tts_stt_backend/services/tts_service.py

#latest
# import os
# import uuid
# import asyncio
# from tts_stt_backend.config.settings import TTS_ENGINE, AUDIO_DIR

# def text_to_speech(text: str) -> str:
#     os.makedirs(AUDIO_DIR, exist_ok=True)

#     filename = f"{uuid.uuid4()}.mp3"
#     output_path = os.path.join(AUDIO_DIR, filename)

#     coro = TTS_ENGINE.synthesize(text, output_path)

#     try:
#         loop = asyncio.get_running_loop()
#         # We are inside FastAPI event loop
#         loop.create_task(coro)
#     except RuntimeError:
#         # No event loop (CLI / sync context)
#         asyncio.run(coro)

#     return f"/audio/{filename}"

import uuid
from tts_stt_backend.config.settings import TTS_ENGINE, AUDIO_DIR

async def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4()}.mp3"
    output_path = AUDIO_DIR / filename

    # 🔒 BLOCK until audio is fully written
    await TTS_ENGINE.synthesize(text, str(output_path))

    # 🔐 safety check
    if not output_path.exists() or output_path.stat().st_size == 0:
        raise RuntimeError("TTS audio generation failed")

    return f"/audio/{filename}"
