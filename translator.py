import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐")

st.title("🌐 Streamlit Language Translator")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

text = st.text_area("Enter text to translate:")

target_language = st.selectbox(
    "Translate to:",
    list(languages.keys())
)

if st.button("Translate"):
    if text.strip():
        try:
            translated = GoogleTranslator(
                source="auto",
                target=languages[target_language]
            ).translate(text)

            st.subheader("Translated Text")
            st.success(translated)

        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text.")