import streamlit as st
from google.oauth2 import id_token
from google.auth.transport import requests

def main():
    st.title("Your Streamlit App")
    st.write("test")
    
    # Google Authentication
    st.subheader("Google Authentication")
    client_id = "896294200925-51fbg1jbp78v7t2f3t1afpguq0vkjbon.apps.googleusercontent.com"  # Replace with your OAuth client ID
    token = st.text_input("Enter your Google ID token", type="password")
    if st.button("Authenticate"):
        try:
            idinfo = id_token.verify_oauth2_token(token, requests.Request(), client_id)
            if idinfo['aud'] != client_id:
                raise ValueError("Invalid client ID")
            st.success(f"Authentication successful: {idinfo['name']}")
            # Continue with the rest of your app logic here
        except ValueError as e:
            st.error("Authentication failed")
            st.error(e)
    
    # Other app content
    # ...
    
if __name__ == "__main__":
    main()