# -----------------------------
# Chatbot
# -----------------------------
st.subheader("💬 Ask a Farming Question")

question = st.text_input(
    "Type your question",
    placeholder="Example: Should I irrigate today?"
)


if "answer" not in st.session_state:
    st.session_state.answer = ""


if st.button("Ask"):

    if question.strip():

        st.session_state.answer = answer_question(
            question,
            crop,
            today
        )

        with st.chat_message("user"):
            st.write(question)

        with st.chat_message("assistant"):
            st.write(st.session_state.answer)

    else:
        st.warning("Please enter a question.")


# -----------------------------
# Translation Feature
# -----------------------------
if st.session_state.answer:

    st.divider()

    st.subheader("🌐 Translate Advisory")

    languages = {
        "Tamil": "ta",
        "Hindi": "hi",
        "Telugu": "te",
        "Malayalam": "ml",
        "Kannada": "kn",
        "English": "en"
    }


    selected_language = st.selectbox(
        "Select Language",
        list(languages.keys())
    )


    if st.button("Translate Answer"):

        translated_text = GoogleTranslator(
            source="auto",
            target=languages[selected_language]
        ).translate(
            st.session_state.answer
        )

        st.success(translated_text)