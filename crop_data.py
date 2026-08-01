import streamlit as st

st.set_page_config(page_title="Crop Selection", page_icon="🌾")

st.title("🌾 Crop Selection")

crops = [
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

selected_crops = st.multiselect(
    "🌱 Select one or more crops",
    crops
)

if selected_crops:
    st.success("Selected Crops:")
    for crop in selected_crops:
        st.write(f"✅ {crop}")
else:
    st.info("Please select at least one crop.")
