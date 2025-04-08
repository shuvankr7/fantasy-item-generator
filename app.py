from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, time

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

start_time = time.time()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForCausalLM.from_pretrained("shuvankar/fantasy-item-model2")
tokenizer = AutoTokenizer.from_pretrained("shuvankar/fantasy-item-model2")

@app.get("/generate")
def generate(prompt: str):
    try:
        full_prompt = f"Input: {prompt} → Output:"
        inputs = tokenizer(full_prompt, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_new_tokens=30, do_sample=True, top_k=50, temperature=0.9)
        result = tokenizer.decode(outputs[0], skip_special_tokens=True)
        clean_output = result.split("→ Output:")[-1].strip() if "→ Output:" in result else result.strip()
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
