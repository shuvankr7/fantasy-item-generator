# app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, time

app = FastAPI()
start_time = time.time()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForCausalLM.from_pretrained("fantasy_item_model2").to(device)
tokenizer = AutoTokenizer.from_pretrained("fantasy_item_model2")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate")
def generate(prompt: str):
    try:
        # Prompt engineering: structured format
        full_prompt = f"Input: {prompt} \u2192 Output:"
        inputs = tokenizer(full_prompt, return_tensors="pt").to(device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=30,
            do_sample=True,
            top_k=50,
            temperature=0.9
        )

        result = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract only the portion after the output marker
        if "\u2192 Output:" in result:
            clean_output = result.split("\u2192 Output:")[-1].strip()
        else:
            clean_output = result.strip()

        return {"output": clean_output}

    except Exception as e:
        return {"error": str(e)}

@app.get("/status")
def status():
    uptime = time.time() - start_time
    return {
        "status": "running",
        "model": "fantasy_item_model2",
        "device": str(device),
        "uptime": f"{uptime:.2f} seconds"
    }
