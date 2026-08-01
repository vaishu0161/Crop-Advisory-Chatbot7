import streamlit as st

st.title("🌾 Crop Advisory System")

crop = st.selectbox(
    "🌱 Select Your Crop",
    [
        "Paddy",
        "Sugarcane",
        "Groundnut",
        "Maize",
        "Cotton",
        "Banana",
        "Tomato",
        "Onion",
        "Chilli",
        "Brinjal",
        "Potato",
        "Wheat",
        "Millets",
        "Coconut",
        "Mango"
    ]
)

st.write("Selected Crop:", crop)
