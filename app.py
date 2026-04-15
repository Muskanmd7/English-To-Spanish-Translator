import streamlit as st
import re

# 🔹 Step 1: Load dataset
@st.cache_data
def load_data():
    english_sentences = []
    spanish_sentences = []

    with open("spa.txt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                eng = parts[0]
                spa = parts[1]
                english_sentences.append(eng)
                spanish_sentences.append(spa)

    return english_sentences, spanish_sentences


# 🔹 Step 2: Clean text
def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text


# 🔹 Step 3: Create dictionary
@st.cache_data
def create_dict(english_sentences, spanish_sentences):
    translation_dict = {}
    for eng, spa in zip(english_sentences, spanish_sentences):
        translation_dict[clean(eng)] = clean(spa)
    return translation_dict


# Load data
english_sentences, spanish_sentences = load_data()
translation_dict = create_dict(english_sentences, spanish_sentences)


# 🔹 UI
st.title("🌍 English → Spanish Translator")
st.write("Dataset-based simple translator")

# Input box
user_input = st.text_input("Enter English sentence:")

# Translate button
if st.button("Translate"):
    if user_input:
        cleaned = clean(user_input)
        result = translation_dict.get(cleaned, "Translation not found")
        st.success(f"Spanish: {result}")
    else:
        st.warning("Please enter a sentence.")