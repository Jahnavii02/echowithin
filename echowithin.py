# echowithin_app.py

import streamlit as st
import random
import datetime

st.set_page_config(page_title="EchoWithin", layout="centered")

# STYLE 
st.markdown("""
    <style>
    .big-font {
        font-size: 20px;
        font-weight: 500;
        color: #3c3c3c;
    }
    .journal-box {
        background-color: #f5f0ff; /* changed from white to soft lavender */
        color: #4b3b5a; /* deep muted purple for contrast */
        padding: 1.2em;
        border-radius: 12px;
        box-shadow: 0px 0px 10px #d8cbe9;
        margin-top: 1em;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)


#  TITLE 
st.title("🌿 EchoWithin")
st.markdown("_A quiet space to hear yourself again._")

#  QUOTE OF THE DAY
quotes = [
    "You are not a drop in the ocean. You are the entire ocean in a drop. — Rumi",
    "The quieter you become, the more you are able to hear. — Ram Dass",
    "Be still. The quieter you become, the more you can hear your own soul. — Unknown",
    "Nothing ever goes away until it teaches us what we need to know. — Pema Chödrön",
]
st.markdown(f"✨ _Quote of the Day:_ **{random.choice(quotes)}**")

#  INPUT SECTION 
st.markdown("### 📝 How are you feeling today?")
user_input = st.text_area("Write here:", height=180, placeholder="I don't know what I'm feeling, but I want to understand...")

#  JOURNAL RESPONSE
def generate_reflection(prompt):
    reflections = [
        f"🪞 Let's gently explore that: _What part of you is speaking the loudest right now?_",
        f"💭 Maybe ask yourself: _What would I tell a friend who felt this way?_",
        f"🌱 EchoWithin wonders: _What emotion is hidden underneath those words?_",
        f"🕊️ Try sitting with this thought: _What is my body trying to express that words cannot?_",
    ]
    return random.choice(reflections)

#  ON CLICK 
if st.button("Reflect with EchoWithin"):
    if user_input.strip():
        st.markdown("### 🌿 EchoWithin Reflects:")
        st.markdown(f"<div class='journal-box'>{generate_reflection(user_input)}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please write something to reflect on.")

#  JOURNAL EXPORT 
if user_input.strip():
    journal_entry = f"Date: {datetime.date.today()}\n\nYou wrote:\n{user_input}\n\nEchoWithin’s reflection:\n{generate_reflection(user_input)}"
    st.download_button("📥 Download Journal Entry", journal_entry, file_name="EchoWithin_Reflection.txt")

#  FOOTER 
st.markdown("---")
st.markdown("🔒 Your reflections stay private. EchoWithin is a calm space for you alone.")
