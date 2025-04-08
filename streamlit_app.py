import streamlit as st
import requests

st.set_page_config(page_title="🧙 Fantasy Item Generator")
st.title("🧙 Fantasy Item Generator")
st.markdown("Enter a fantasy prompt like `ice element`, `staff of fire`, or `arcane shield`")

prompt = st.text_input("Your fantasy prompt:")

if st.button("🔮 Generate"):
    if not prompt.strip():
        st.warning("Please enter a valid prompt.")
    else:
        with st.spinner("Summoning item..."):
            try:
                response = requests.get("http://localhost:8000/generate", params={"prompt": prompt})
                data = response.json()
                if "output" in data:
                    st.success(f"🛡️ {data['output']}")
                else:
                    st.error(f"❌ Error: {data.get('error', 'Unknown error')}")
            except Exception as e:
                st.error("⚠️ Could not connect to backend. Is FastAPI running?")
                st.exception(e)
