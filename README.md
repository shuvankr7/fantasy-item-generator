------ Fantasy Item Generator

LIVE APP LINK - https://fantasy-item-generator-vnqjy5v3msme7qpzram9gz.streamlit.app/


This project uses a fine-tuned language model to generate fantasy item names based on creative prompts like *"ice staff"*, *"arcane shield"*, or *"dark sword"*. It’s built with 🤗 Transformers and deployed with Streamlit.

Model is trained on data2.csv, data is generated manually and using LLM.

------ Features

- Fantasy item name generation from short text prompts.
- Fine-tuned GPT-2 on fantasy-themed inputs/outputs.
- Web UI using Streamlit
- 🤗-hosted model loading.


----- Setup & Installation

-- 1. Clone the repository

https://github.com/shuvankr7/fantasy-item-generator.git

pip install -r requirements.txt

streamlit run app.py


 ----- Model Files

This app uses a model uploaded to the Hugging Face Hub:

LINK -  https://huggingface.co/shuvankar/fantasy-item-model2

All model files (config.json, model.safetensors, tokenizer.json, etc.) are hosted there.

If you're running offline or want to avoid fetching from Hugging Face every time:

Download the model from the link above.

    model = AutoModelForCausalLM.from_pretrained("shuvankar/fantasy-item-model2")
    tokenizer = AutoTokenizer.from_pretrained("shuvankar/fantasy-item-model2")

    
You can use api.py and index.html to run it in local aswell




💡 Example Prompt
Input: Wand, ice element
Output: Frostbinder Wand of Shattered Light

📜 License
MIT License. Feel free to use, modify, and share!

✨ Author
Shuvankar - https://www.linkedin.com/in/shuvankar-naskar-data-scientist

