import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import time

# Setup
start_time = time.time()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained("shuvankar/fantasy-item-model2").to(device)
    tokenizer = AutoTokenizer.from_pretrained("shuvankar/fantasy-item-model2")
    return model, tokenizer

model, tokenizer = load_model()

# Streamlit UI
st.set_page_config(page_title="🧙 Fantasy Item Generator")
st.title("🧙 Fantasy Item Generator")
st.write("Enter a fantasy prompt like `ice element`, `staff of fire`, or `arcane shield`")

prompt = st.text_input("Your fantasy prompt:")
generate = st.button("🔮 Generate")

if generate and prompt.strip():
    with st.spinner("Conjuring item from the arcane library..."):
        try:
            full_prompt = f"Input: {prompt} → Output:"
            inputs = tokenizer(full_prompt, return_tensors="pt").to(device)
            outputs = model.generate(
                **inputs,
                max_new_tokens=30,
                do_sample=True,
                top_k=50,
                temperature=0.9
            )
            result = tokenizer.decode(outputs[0], skip_special_tokens=True)
            output = result.split("→ Output:")[-1].strip() if "→ Output:" in result else result.strip()
            st.success(f"🛡️ {output}")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
elif generate:
    st.warning("⚠️ Please enter a prompt.")
    
