# CodeToGive - Petopia
Team 1 Code to Give -- Morgan Stanley

## Overview

Welcome to the Petopia! This interactive application was developed as a solution to a technical challenge aimed at creating an entertaining, engaging, and accessible sensory experience for children and young people referred to CHAS (Children's Hospices Across Scotland). The app allows users to design their own augmented reality (AR) pet using various input methods, including voice, text, and sign language. Designed with a child-friendly interface, the app aims to bring moments of joy to its users.

## Features

1. **Login/Signup Page**: Users can log in using Google or Facebook or sign up for a new account.
2. **Pet Design Page**: Users can choose to design their own pet or select from pre-designed pets.
3. **Input Method Selection**: Users can choose their preferred method of input:
   - Voice Input: Speak to design your pet.
   - Text Input: Type to design your pet.
   - Sign Language Input: Use Makaton sign language to design your pet.
4. **Pet Choice Page**: If users opt for a pre-designed pet, they can select from a variety of available pets.
5. **Image Generation**: Based on the user's input, an image of the pet is generated using OpenAI.
6. **Immerse in AR**: Experience and interact with the pets through AR. Users can make the pets do tricks & feed them.

## Setup

### Prerequisites

- Python 3.x
- Streamlit
- OpenAI API key
- Google Speech Recognition

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PeiPeiC/CodeToGive-ARPet.git
   ```

2. Navigate to the project directory:
   ```bash
   cd AR-Pet-Game
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key. You can either set it as an environment variable or directly in the code:
   ```bash
   export OPENAI_API_KEY=your_api_key
   ```

### Running the App

To run the app, simply execute the following command:

```bash
streamlit run streamlit_app.py
```

Open the provided URL in your browser to access the AR Pet Game.

## Usage

1. **Login/Signup**: Start by logging in or signing up.
2. **Design Your Pet**: Choose whether you'd like to design your own pet or use a pre-designed one.
3. **Choose Input Method**: If you opt to design your own pet, select your preferred input method.
4. **Provide Input**: Depending on your chosen method, provide the necessary input to design your pet.
5. **View Your Pet**: Once you've provided your input, the app will generate and display an image of your pet.

## Output & Demonstration

**Our website**

https://github.com/PeiPeiC/CodeToGive-ARPet/assets/104357328/e8c997f1-fcca-40c6-a8b9-9025d47e4018

**The AR experience**


https://github.com/PeiPeiC/CodeToGive-ARPet/assets/97734079/8472fb07-ea26-41bf-84cb-69509b8b391b

In the AR experience, we can interact with the generated pet. Currently we can make them do tricks and feed them with some food. In the future, we would like to expand these features to include more interactions such as the pet being able to tell stories for the kids, pet customizations, and the ability to interact with other's pet no matter where they live.

Demo Links:
**Instagram:** https://www.instagram.com/ar/1690152044804497/
**Facebook:** https://www.facebook.com/fbcameraeffects/tryit/1690152044804497/

## Customization

- **Icons**: You can replace the icons in the `ICONS` dictionary with your own icons. Make sure to update the paths accordingly.
- **Styles**: Customize the app's appearance by modifying the CSS in the `st.markdown` section.

## Troubleshooting

- **API Key Issues**: Ensure that your OpenAI API key is correctly set up. If you're facing issues, try regenerating the key from the OpenAI dashboard.
- **Audio Recognition**: If the voice input isn't recognized, ensure you have a stable internet connection and speak clearly.


## Acknowledgments

- OpenAI for image generation.
- Google Speech Recognition for voice input processing.
- Meta Spark Studio for AR effects implementation
- "Quirky Series - FREE Animals Pack" (https://skfb.ly/oHtnQ) by Omabuarts Studio is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).
- "Fruits N' Stuff" (https://skfb.ly/6X7tA) by AlienDev is licensed under Creative Commons Attribution (http://creativecommons.org/licenses/by/4.0/).

Enjoy designing your AR pet! 🐾

