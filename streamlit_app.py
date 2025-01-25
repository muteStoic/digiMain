import streamlit as st
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

# Authenticate Google Drive
@st.cache_resource
def authenticate_google_drive():
    gauth = GoogleAuth()
    gauth.DEFAULT_SETTINGS['client_config_file'] = 'client_secret_896294200925-51fbg1jbp78v7t2f3t1afpguq0vkjbon.apps.googleusercontent.com.json'  # Add your JSON file here
    gauth.LoadCredentialsFile("credentials.txt")
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()  # Authenticate if no credentials
    elif gauth.access_token_expired:
        gauth.Refresh()  # Refresh credentials if expired
    else:
        gauth.Authorize()  # Authorize if valid
    gauth.SaveCredentialsFile("credentials.txt")
    return GoogleDrive(gauth)

# Initialize Google Drive
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
