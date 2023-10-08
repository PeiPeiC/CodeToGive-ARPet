import base64
import streamlit as st
from audio_recorder_streamlit import audio_recorder
import speech_recognition as sr
import openai
import tempfile
from pydub import AudioSegment
import io
import os

# Constants
ICONS = {
    "Voice Input": "./icons/microphone_icon.png",
    "Text Input": "./icons/keyboard_icon.png",
    "Sign Language Input": "./icons/hand_icon.png"
}

# Define function to create a data URI for an image
def image_to_data_uri(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Load icons
mic_icon = image_to_data_uri("./icons/microphone_icon.png")
keyboard_icon = image_to_data_uri("./icons/keyboard_icon.png")
hand_icon = image_to_data_uri("./icons/hand_icon.png")


def display_login_page():
    st.title("Welcome to AR Pet Game!")
    st.subheader("Please login or signup to continue.")
    
    # Using session state to detect button clicks
    login_methods = ["Login with Google", "Login with Facebook", "Signup"]
    for method in login_methods:
        if st.button(method):
            st.session_state['logged_in'] = True

def display_pet_design_page():
    st.title("Design Your Pet!")
    st.subheader("Choose how you'd like to design your pet.")
    
    pet_designs = ["Design My Own Pet", "Use Pre-designed Pet"]
    for design in pet_designs:
        if st.button(design):
            st.session_state['pet_design'] = design

def display_input_method_page():
    st.title("Choose Your Input Method")
    for method, icon_path in ICONS.items():
        icon_data = image_to_data_uri(icon_path)
        if st.button(method):
            st.session_state['input_method'] = method.lower().replace(" ", "_")
        st.markdown(f"""
        <style>
            .btn-md {{ visibility: hidden; }}
        </style>
        <div>
            <a class="icon-button">
                <img src="data:image/png;base64,{icon_data}" alt="{method}">
                {method}
            </a>
        </div>
        """, unsafe_allow_html=True)

def display_pet_choice_page():
    st.title("Choose Your Pet")
    
    pets = ["Pet 1", "Pet 2", "Pet 3"]
    for pet in pets:
        if st.button(pet):
            st.write(f"You chose {pet}!")

# Set child-friendly styles
st.markdown(
    """
    <style>
        body {
            background-color: #FFDAB9; /* Peach background */
            font-family: 'Comic Sans MS', 'Chalkboard SE', 'Marker Felt'; /* Fun font */
        }
        h1, h2 {
            color: #E69966; /* Bright  titles */
            text-align: center;
        }
        .icon-button {
            padding: 15px 30px;
            font-size: 20px;
            border: none;
            background-color: #FEC773; /*  background colour for buttons */
            cursor: pointer;
            display: block; /* Make buttons block-level elements */
            width: 80%; /* Set a fixed width */
            margin: 10px auto; /* Center the buttons and add margin */
            text-align: center;
            border-radius: 15px;
            transition: background-color 0.3s;
        }
        .icon-button img {
            width: 30px;
            height: 30px;
        }
        .icon-button:hover {
            background-color: #E69966; /* Chartreuse color on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to generate image from text using OpenAI
def generate_image_from_text(user_input):
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
        st.image(image_bytes, caption="Generated Image", use_column_width=True)
    except Exception as e:
        # Print the exception details for debugging
        print(f"Error: {e}")
        st.error("Oops! Something went wrong while generating the image. Please try again later.")

def convert_to_wav(audio_bytes):
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    temp_audio_filename = tempfile.mktemp(suffix=".wav")
    audio.export(temp_audio_filename, format="wav")
    return temp_audio_filename

def get_text_from_audio(audio_bytes):
    r = sr.Recognizer()
    # Convert audio to WAV format
    wav_filename = convert_to_wav(audio_bytes)    
    try:
        with sr.AudioFile(wav_filename) as source:
            audio_data = r.record(source)
            try:
                text = r.recognize_google(audio_data)
                return text
            except sr.UnknownValueError:
                st.error("Google Speech Recognition could not understand the audio.")
            except sr.RequestError:
                st.error("Could not request results from Google Speech Recognition service.")
    finally:
        # Ensure the temporary file is deleted
        os.remove(wav_filename)    
    return None

def handle_voice_input():
    audio_bytes = audio_recorder()
    if audio_bytes:
        user_input = get_text_from_audio(audio_bytes)
        if user_input:
            generate_image_from_text(user_input)

def handle_text_input():
    user_input = st.text_input("Type Here:")
    if user_input:
        generate_image_from_text(user_input)

def handle_sign_language_input():
    st.camera_input("Capture Makaton Sign Language")


def main():
    # Custom-styled buttons overlaying the Streamlit buttons
    st.write("")  # Add an empty line for spacing
    col1, col2, col3 = st.columns([1, 6, 1])   # Create columns to center the content
    with col2:  # Use the center column to display the content
        if not st.session_state.get('logged_in', False):
            display_login_page()
        elif not st.session_state.get('pet_design'):
            display_pet_design_page()
        else:
            if st.session_state['pet_design'] == "Design My Own Pet":
                display_input_method_page()
                if st.session_state.get('input_method') == 'voice_input':
                    handle_voice_input()
                elif st.session_state.get('input_method') == 'text_input':
                    handle_text_input()
                elif st.session_state.get('input_method') == 'sign_language_input':
                    handle_sign_language_input()
            else:
                display_pet_choice_page()

if __name__ == "__main__":
    main()