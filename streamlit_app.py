import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os
import json

# Authenticate Google Drive (This will ask for OAuth the first time)
def authenticate_google_drive():
    client_secret = st.secrets["client_secret"]
    with open('client_secret.json', 'w') as f:
        json.dump(client_secret, f)

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # This will prompt for OAuth the first time
    return GoogleDrive(gauth)

# Initialize Google Drive
drive = authenticate_google_drive()

# Streamlit UI
st.title("Upload to Google Drive")
uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file:
    folder_id = "YOUR_GOOGLE_DRIVE_FOLDER_ID"  # Replace with your folder ID
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
