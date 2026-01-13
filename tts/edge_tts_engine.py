# # # # import asyncio
# # # # import edge_tts
# # # # from tts.base import BaseTTS


# # # # class EdgeTTSEngine(BaseTTS):
# # # #     def speak(self, text: str, output_file: str):
# # # #         async def _generate():
# # # #             communicate = edge_tts.Communicate(
# # # #                 text=text,
# # # #                 voice="en-IN-PrabhatNeural"
# # # #             )
# # # #             await communicate.save(output_file)

# # # #         asyncio.run(_generate())

# # # import asyncio
# # # import edge_tts
# # # from tts.base import BaseTTSEngine

# # # class EdgeTTSEngine(BaseTTSEngine):

# # #     async def _generate(self, text: str, output_path: str):
# # #         communicate = edge_tts.Communicate(
# # #             text=text,
# # #             voice="en-IN-PrabhatNeural"
# # #         )
# # #         await communicate.save(output_path)

# # #     def synthesize(self, text: str, output_path: str) -> None:
# # #         asyncio.run(self._generate(text, output_path))


# # import asyncio
# # import edge_tts
# # from tts_stt_backend.tts.base import BaseTTS

# # class EdgeTTSEngine(BaseTTS):

# #     async def _run(self, text: str, output_path: str):
# #         communicate = edge_tts.Communicate(
# #             text=text,
# #             voice="en-US-AriaNeural"
# #         )
# #         await communicate.save(output_path)

# #     async def synthesize(self, text: str, output_path: str):
# #         await self._run(text, output_path)


# import asyncio
# import edge_tts
# from tts_stt_backend.tts.base import BaseTTS


# class EdgeTTSEngine(BaseTTS):
#     def __init__(self, voice: str = "en-US-AriaNeural"):
#         self.voice = voice

#     async def _run(self, text: str, output_path: str):
#         communicate = edge_tts.Communicate(text, self.voice)
#         await communicate.save(output_path)

#     def synthesize(self, text: str, output_path: str) -> None:
#         """
#         Safe for FastAPI:
#         - If event loop exists → schedule task
#         - Else → run normally
#         """
#         try:
#             loop = asyncio.get_running_loop()
#             loop.create_task(self._run(text, output_path))
#         except RuntimeError:
#             asyncio.run(self._run(text, output_path))


# tts_stt_backend/tts/edge_tts_engine.py
import edge_tts
from tts_stt_backend.tts.base import BaseTTS

class EdgeTTSEngine(BaseTTS):

    async def _run(self, text: str, output_path: str):
        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural"
        )
        await communicate.save(output_path)

    
    def synthesize(self, text: str, output_path: str):
        return self._run(text, output_path)  
