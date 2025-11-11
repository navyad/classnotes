import streamlit as st
import requests

st.title("ClassNotes PDF Uploader")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    st.write(f"Uploading `{uploaded_file.name}`...")
    
    # Send PDF to FastAPI backend
    files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
    response = requests.post("http://localhost:8000/notes/upload", files=files)
    if response.status_code == 200:
        st.success("PDF processed successfully!")
        st.json(response.json())  # Display extracted notes or note ID
    else:
        st.error(f"Error: {response.text}")

