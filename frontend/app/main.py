import streamlit as st 
import requests 
from streamlit_quill import st_quill

backend_url = "http://localhost:8000"

def add_note(content):
    try:
        response = requests.post(
            f"{backend_url}/api/notes/",
            json={"content": content}) 
        response.raise_for_status()
        return response.json() 
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching notes: {e}")
        return [] 
    
def note_editor():
    content = st_quill(
        placeholder="Write your note here...",
        html=True,
        key="note_editor"
    )
    if content:
        response = add_note(content)
        if response:
            st.success("Note added successfully!")
            st.json(response)  # Display the response in JSON format
            return response["content"]  # Return the content of the note
        else:
            st.error("Failed to add note.")
    return None

def main():
    st.title("Kubenotes")
    st.write("Application for managing notes using Kubernetes and Docker.") 
    # get_notes = st.button("Fetch Notes")
    # if get_notes:
    note_editor() 

    # Add more Streamlit components as needed
    st.sidebar.header("Navigation")
    st.sidebar.write("Use the sidebar to navigate through the application.") 

main()