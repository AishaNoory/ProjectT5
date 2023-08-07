import streamlit as st
import requests

# Streamlit app title
st.title("Case File Summarizer")

# User input: case file identifier or query
user_input = st.text_input("Enter case file identifier or query:")

# Summarization button
if st.button("Get Summary"):
    if user_input:
        # Send a request to your model API to retrieve the summary
        model_api_url = " https://23b0-196-216-70-186.ngrok-free.app/summarize"  # Replace with your actual model API URL
        payload = {"input": user_input}
        
        try:
            response = requests.post(model_api_url, json=payload)
            if response.status_code == 200:
                summary = response.json()["summary"]
                st.subheader("Summary:")
                st.write(summary)
            else:
                st.error("Error: Unable to retrieve summary.")
        except requests.RequestException as e:
            st.error("Error: Unable to connect to the model API.")
    else:
        st.warning("Please enter a case file identifier or query.")
