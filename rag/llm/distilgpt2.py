import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from tts_stt_backend.rag.llm.base import BaseLLM

class DistilGPT2LLM(BaseLLM):

    def __init__(self):
        model_path = "tts_stt_backend/models/distilgpt2"

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
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                pad_token_id=self.tokenizer.eos_token_id
            )

        decoded = self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

        return decoded.split("Answer:")[-1].strip()
