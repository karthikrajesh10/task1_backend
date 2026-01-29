# from transformers import pipeline
# from tts_stt_backend.rag.llm.base import BaseLLM

# class Phi2LLM(BaseLLM):

#     def __init__(self):
#         self.pipe = pipeline(
#             "text-generation",
#             model="microsoft/phi-2",
#             max_new_tokens=200
#         )

#     def generate(self, prompt: str) -> str:
#         result = self.pipe(prompt)[0]["generated_text"]
#         return result.split("Answer:")[-1].strip()


# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
# from tts_stt_backend.rag.llm.base import BaseLLM


# class Phi2LLM(BaseLLM):
#     """
#     Offline Phi-2 LLM wrapper
#     """

#     def __init__(self):
#         model_path = "tts_stt_backend/models/phi-2"

#         self.tokenizer = AutoTokenizer.from_pretrained(
#             model_path,
#             local_files_only=True
#         )

#         self.model = AutoModelForCausalLM.from_pretrained(
#             model_path,
#             torch_dtype=torch.float32,
#             device_map="cpu",
#             local_files_only=True
#         )

#         self.model.eval()

#     def generate(self, prompt: str) -> str:
#         inputs = self.tokenizer(
#             prompt,
#             return_tensors="pt"
#         )

#         with torch.no_grad():
#             outputs = self.model.generate(
#                 **inputs,
#                 max_new_tokens=200,
#                 do_sample=False
#             )

#         text = self.tokenizer.decode(
#             outputs[0],
#             skip_special_tokens=True
#         )

#         return text.split("Answer:")[-1].strip()


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tts_stt_backend.rag.llm.base import BaseLLM


class Phi2LLM(BaseLLM):
    """
    Offline Phi-2 LLM (CPU-only, no accelerate)
    """

    def __init__(self):
        model_path = "tts_stt_backend/models/phi-2"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            local_files_only=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            local_files_only=True
        )

        self.model.eval()

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=200,
                do_sample=False
            )

        text = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return text.split("Answer:")[-1].strip()
