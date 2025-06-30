import streamlit as st 
import requests 
from streamlit_quill import st_quill

backend_url = "http://localhost:8000"

# Function to add a note to the backend
# This function sends a POST request to the backend to add a note
def add_note(payload):
    try:
        response = requests.post(
            f"{backend_url}/api/notes/",
            json = payload
        )
        response.raise_for_status() 
        return response.json()  
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching notes: {e}")
        return [] 
    
def note_editor():
    # Streamlit components for the note editor 
    st.header("Create a New Note")
    title = st.text_input("Note Title", placeholder = "Enter title (optional)")
    tags = st.text_input("Tags (comma separated)", placeholder = "e.g. ML, Kubernetes")
    is_pinned = st.checkbox("📌 Pin this note") 

    # Function to render the note editor using Streamlit Quill
    content = st_quill(
        placeholder = "Write your note here...",
        html = True,
        key = "note_editor"
    )

    if st.button("Create Note") and content:
        payload = {
            "title": title,
            "content": content,
            "tags": [tag.strip() for tag in tags.split(",") if tag.strip()],
            "is_pinned": is_pinned
        }
        st.write("Sending payload:", payload)
        response = add_note(payload)
        if response:
            st.success("Note added successfully!")
        else:
            st.error("Failed to add note.")

def main():
    st.set_page_config(
        page_title = "Kubenotes",
        page_icon = "📝",
        layout = "wide"
    )
    st.title("Kubenotes")
    st.write("Application for managing notes using Kubernetes and Docker.") 

    note_editor() 

    # Add more Streamlit components as needed
    st.sidebar.header("Navigation")
    st.sidebar.write("Use the sidebar to navigate through the application.") 

if __name__ == "__main__":
    main()