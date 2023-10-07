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

# Create three columns for the buttons
col1, col2, col3 = st.columns(3)

# Display microphone icon for voice input in the first column
with col1:
    mic_icon = image_to_data_uri("./icons/microphone_icon.png")
    if st.button("Voice Input", key="voice_button"):
        st.write("Voice input selected!")
    st.markdown(f'<img src="data:image/jpeg;base64,{mic_icon}" width="80" style="display: block; margin: 0 auto;">', unsafe_allow_html=True)

# Display keyboard icon for text input in the second column
with col2:
    keyboard_icon = image_to_data_uri("./icons/keyboard_icon.png")
    if st.button("Text Input", key="text_button"):
        st.write("Text input selected!")
    st.markdown(f'<img src="data:image/png;base64,{keyboard_icon}" width="80" style="display: block; margin: 0 auto;">', unsafe_allow_html=True)

# Display hand icon for sign language input in the third column (assuming you have this section in your code)
with col3:
    hand_icon = image_to_data_uri("./icons/hand_icon.png")
    if st.button("Sign Language Input", key="sign_language_button"):
        st.write("Sign language input selected!")
    st.markdown(f'<img src="data:image/png;base64,{hand_icon}" width="80" style="display: block; margin: 0 auto;">', unsafe_allow_html=True)


# Add some spacing before the footer
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("Code to give Team 1 ")
# Display footer
st.markdown(
    """
    <footer style="padding: 10px; background-color: #FFA07A; text-align: center;">
        AR Pet Game &copy; 2023
    </footer>
    """,
    unsafe_allow_html=True,
)
