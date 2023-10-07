import streamlit as st
from PIL import Image as PILImage
import io
import base64
import openai
import requests

# Define function to create a data URI for an image
def image_to_data_uri(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Set page title and layout
st.set_page_config(page_title="AR Pet Game", layout="centered", initial_sidebar_state="collapsed")

# Set background color and custom CSS styles
st.markdown(
    """
    <style>
        body {
            background-color: #FFDDC1;
        }
        .icon-button {
            padding: 10px 20px;
            border: none;
            background-color: #f5f5f5;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .icon-button img {
            width: 20px;
            height: 20px;
        }
        .icon-button:hover {
            background-color: #e0e0e0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Check if user has chosen pet design
if 'pet_design' not in st.session_state:
    st.session_state['pet_design'] = None

# Login/Signup Page
if not st.session_state['logged_in']:
    st.title("Welcome to AR Pet Game!")
    st.subheader("Please login or signup to continue.")
    
    # Using session state to detect button clicks
    if 'google_clicked' not in st.session_state:
        st.session_state['google_clicked'] = False
    if 'facebook_clicked' not in st.session_state:
        st.session_state['facebook_clicked'] = False
    if 'signup_clicked' not in st.session_state:
        st.session_state['signup_clicked'] = False

    # Display buttons and check for clicks
    if st.button("Login with Google"):
        st.session_state['google_clicked'] = True
    if st.button("Login with Facebook"):
        st.session_state['facebook_clicked'] = True
    if st.button("Signup"):
        st.session_state['signup_clicked'] = True

    # Handle button clicks
    if st.session_state['google_clicked']:
        st.session_state['logged_in'] = True
        st.session_state['google_clicked'] = False  # Reset the button state
    if st.session_state['facebook_clicked']:
        st.session_state['logged_in'] = True
        st.session_state['facebook_clicked'] = False  # Reset the button state
    if st.session_state['signup_clicked']:
        st.session_state['logged_in'] = True
        st.session_state['signup_clicked'] = False  # Reset the button stat
# Pet Design Selection Page
elif st.session_state['pet_design'] is None:
    st.title("Design Your Pet!")
    st.subheader("Choose how you'd like to design your pet.")
    
    if st.button("Design My Own Pet"):
        st.session_state['pet_design'] = 'custom'
    if st.button("Use Pre-designed Pet"):
        st.session_state['pet_design'] = 'premade'

# Input Selection or Pre-designed Pets Page
else:
    if st.session_state['pet_design'] == 'custom':
        st.title("Choose Your Input Method")
        
        # Define the icons
        mic_icon = image_to_data_uri("./icons/microphone_icon.png")
        keyboard_icon = image_to_data_uri("./icons/keyboard_icon.png")
        hand_icon = image_to_data_uri("./icons/hand_icon.png")
        
        col1, col2, col3 = st.columns(3)
        
        # Display microphone icon for voice input in the first column
        with col1:
            st.markdown(f"""
            <button class="icon-button">
                <img src="data:image/png;base64,{mic_icon}" alt="Microphone Icon">
                Voice Input
            </button>
            """, unsafe_allow_html=True)
            # Connect to Whisper API for speech-to-text (for this mockup, we'll use a text input)
            st.text_input("Speak Now:")
        
        # Display keyboard icon for text input in the second column
        with col2:
            st.markdown(f"""
            <button class="icon-button">
                <img src="data:image/png;base64,{keyboard_icon}" alt="Keyboard Icon">
                Text Input
            </button>
            """, unsafe_allow_html=True)
            user_input = st.text_input("Type Here:")
    
            if user_input:
                st.write("Generating pet...")
                try:
                    openai.api_key = "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"

                    res = openai.Image.create(
                        prompt=user_input,
                        n=1,
                        size="1024x1024",
                        response_format="b64_json"
                    )

                    generated_image_data = res['data'][0]['b64_json']

                    image_bytes = base64.b64decode(generated_image_data)

                    st.image(image_bytes, caption="Magic Image ", use_column_width=True)

                except Exception as e:
                    st.error("Oops! Something went wrong while generating the image. Please try again later. ")

        
        # Display hand icon for sign language input in the third column
        with col3:
            st.markdown(f"""
            <button class="icon-button">
                <img src="data:image/png;base64,{hand_icon}" alt="Hand Icon">
                Sign Language Input
            </button>
            """, unsafe_allow_html=True)
            # Placeholder for sign language input
            st.write("Sign language input selected!")
    
    elif st.session_state['pet_design'] == 'premade':
        st.title("Choose Your Pet")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Pet 1"):
                st.write("You chose Pet 1!")
        with col2:
            if st.button("Pet 2"):
                st.write("You chose Pet 2!")
        with col3:
            if st.button("Pet 3"):
                st.write("You chose Pet 3!")
