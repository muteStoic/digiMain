import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import json


def authenticate_google_drive():
    # Load client_secret directly from Streamlit secrets
    client_secret = st.secrets["client_secret"]
    
    # Write the client_secret to a temporary file
    

    # Authenticate with Google Drive
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile(client_secret)

    # Now you can use `gauth` to interact with Google Drive
    drive = GoogleDrive(gauth)
    return drive

# Authenticate and get the Google Drive object
drive = authenticate_google_drive()


# Streamlit UI
st.title("Upload to Google Drive")
uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file:
    folder_id = "14LNnis-SuY6w56_4dej4xWHpz6RRF43r"  # Replace with your folder ID
    file_name = uploaded_file.name
    st.write(f"Uploading `{file_name}` to Google Drive...")

    # Save the uploaded file temporarily
    with open(file_name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Upload to Google Drive
    gfile = drive.CreateFile({"parents": [{"id": folder_id}], "title": file_name})
    gfile.SetContentFile(file_name)
    gfile.Upload()

    st.success(f"File `{file_name}` successfully uploaded to Google Drive!")

    # Remove the temporary file
    os.remove(file_name)
