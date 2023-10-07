import streamlit as st
import base64

try:
    st.set_page_config(page_title="AR Pet Game", layout="centered", initial_sidebar_state="collapsed")
except Exception:
    pass


# Define function to create a data URI for an image
def image_to_data_uri(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Set child-friendly styles
st.markdown(
    """
    <style>
        body {
            background-color: #FFDAB9; /* Peach background */
            font-family: 'Comic Sans MS', 'Chalkboard SE', 'Marker Felt'; /* Fun font */
        }
        h1, h2 {
            color: #FF69B4; /* Bright pink titles */
        }
        .icon-button {
            padding: 15px 30px;
            font-size: 20px;
            border: none;
            background-color: #ADFF2F; /* GreenYellow background for buttons */
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 15px;
            border-radius: 15px;
            transition: background-color 0.3s;
        }
        .icon-button img {
            width: 30px;
            height: 30px;
        }
        .icon-button:hover {
            background-color: #7FFF00; /* Chartreuse color on hover */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
    
    icons = {
        "Voice Input": "./icons/microphone_icon.png",
        "Text Input": "./icons/keyboard_icon.png",
        "Sign Language Input": "./icons/hand_icon.png"
    }
    
    for method, icon_path in icons.items():
        icon_data = image_to_data_uri(icon_path)
        st.markdown(f"""
        <button class="icon-button">
            <img src="data:image/png;base64,{icon_data}" alt="{method}">
            {method}
        </button>
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
            background-color: #FEC773; /* GreenYellow background for buttons */
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


# Main App Logic
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
        else:
            display_pet_choice_page()