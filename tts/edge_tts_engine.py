import asyncio
import edge_tts
from tts_stt_backend.tts.base import BaseTTS

class EdgeTTSEngine(BaseTTS):
    def speak(self, text: str, output_file: str):
        async def _generate():
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-IN-PrabhatNeural"
            )
            await communicate.save(output_file)

        asyncio.run(_generate())
