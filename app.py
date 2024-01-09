import streamlit as st

# Set the page config to have the title and layout you want
st.set_page_config(page_title="My Enhanced Streamlit App", page_icon="🚀", layout="wide")

# Add a sidebar
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Choose the app mode", ["Home", "About"])

if app_mode == "Home":
    st.title("My Enhanced Streamlit App")
    st.write("Hello, world!")

    # Add a text input for the name
    name = st.text_input("Enter your name:")

    # Add a selectbox for the user's favorite programming language
    language = st.selectbox("Select your favorite programming language", ["Python", "JavaScript", "C++", "Java", "Go"])

    if name:
        st.write(f"Welcome, {name}!")
        st.write(f"Your favorite programming language is {language}.")

elif app_mode == "About":
    st.title("About")
    st.write("This is a simple Streamlit app enhanced with some additional features like a sidebar for navigation and a selectbox for choosing a favorite programming language.")


