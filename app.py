import streamlit as st
import google.generativeai as genai
import os

# 1. API key-ஐ அமைத்தல்
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. இணையப் பக்கத்தின் வடிவமைப்பு
st.title("YASEENIS AI 🤖")

# 3. பழைய உரையாடல்களை சேமிக்க (Memory)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. பழைய மெசேஜ்களை திரையில் காட்ட
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. பயனர் உள்ளீட்டைப் பெற்று பதிலை உருவாக்குதல்
if prompt := st.chat_input("என்னிடம் ஏதாவது கேளுங்கள்..."):
    # பயனர் தட்டச்சு செய்ததைக் காட்ட
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI-இன் பதிலைப் பெற
    response = model.generate_content(prompt)
    
    # AI-இன் பதிலை திரையில் காட்ட
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
