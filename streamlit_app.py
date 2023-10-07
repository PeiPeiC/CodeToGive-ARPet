# Import necessary libraries
import streamlit as st
import base64

# Define function to create a data URI for an image
def image_to_data_uri(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Set page title and layout
st.set_page_config(page_title="AR Pet Game", layout="centered", initial_sidebar_state="collapsed")

# Set background color
st.markdown(
    """
    <style>
        body {
            background-color: #FFDDC1;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display title
st.title("Welcome to AR Pet Game!")

# Display subtitle
st.subheader("Choose your way to play:")

# Display microphone icon for voice input
mic_icon = image_to_data_uri("./icons/microphone_icon.jpg")
if st.button("", on_click=None, help=None, disabled=False, use_container_width=True, key=None):
    st.write("Voice input selected!")
st.markdown(f'<img src="data:image/jpeg;base64,{mic_icon}" width="100">', unsafe_allow_html=True)
st.write("Voice Input")

# Display keyboard icon for text input
keyboard_icon = image_to_data_uri("./icons/keyboard_icon.png")
if st.button("", on_click=None, help=None, disabled=False, use_container_width=True, key=None):
    st.write("Text input selected!")
st.markdown(f'<img src="data:image/png;base64,{keyboard_icon}" width="100">', unsafe_allow_html=True)
st.write("Text Input")

# # Display hand icon for sign language input
# hand_icon = image_to_data_uri("path_to_hand_icon.png")
# if st.button("", on_click=None, help=None, disabled=False, use_container_width=True, key=None):
#     st.write("Sign language input selected!")
# st.markdown(f'<img src="data:image/png;base64,{hand_icon}" width="100">', unsafe_allow_html=True)
# st.write("Sign Language Input")

# Display footer
st.markdown(
    """
    <footer style="position: absolute; bottom: 0; width: 100%; text-align: center; padding: 10px; background-color: #FFA07A;">
        AR Pet Game &copy; 2023
    </footer>
    """,
    unsafe_allow_html=True,
)

