from transformers import pipeline
summarizer = pipeline("summarization")
import streamlit as st
from transformers import pipeline
from gtts import gTTS

st.title("Text Summarizer with Audio")

summarizer = pipeline("summarization")

input_text = st.text_area("Enter your text here:")

if st.button("Summarize"):
    if input_text.strip() == "":
        st.warning("Please enter some text")
    
    elif len(input_text.split()) < 20:
        st.warning("Text is too short for summarization")
    
    else:
        summary = summarizer(
            input_text[:1000],  # limit input
            max_length=100,
            min_length=30,
            do_sample=False
        )

        summary_text = summary[0]['summary_text']
        st.write(summary_text)

        tts = gTTS(summary_text)
        tts.save("summary.mp3")
        st.audio("summary.mp3")