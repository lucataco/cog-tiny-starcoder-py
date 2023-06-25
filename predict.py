from cog import BasePredictor, Input
import torch
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM

device = "cuda"

class Predictor(BasePredictor):
    def setup(self):
        name = 'bigcode/tiny_starcoder_py'
        self.tokenizer = AutoTokenizer.from_pretrained(name, cache_dir="cache")
        self.model = AutoModelForCausalLM.from_pretrained(name, cache_dir="cache").to(device)

    def predict(self,
        prompt: str = Input(description="Instruction for the model"),
        max_new_tokens: int = Input(description="max tokens to generate", default=20)
    ) -> str:    
        inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = self.model.generate(
            inputs, 
            max_new_tokens=max_new_tokens,
            pad_token_id=self.tokenizer.eos_token_id)
        output = self.tokenizer.decode(outputs[0])
        return output
    