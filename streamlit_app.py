import streamlit as st
from transformers import pipeline
st.markdown(""" This is a Streamlit App """)
st.title("Text Summarization App")

# Text input widget
text_input = st.text_area("Enter text to summarize:")

# Summarization options
max_length = st.slider("Max Summary Length", min_value=10, max_value=500, value=150)

# Summarize button
if st.button("Summarize"):
    if text_input:
        summarizer = pipeline("summarization")
        summary = summarizer(text_input, max_length=max_length)[0]['summary_text']
        st.subheader("Summary:")
        st.write(summary)
    else:
        st.warning("Please enter text to summarize.")
