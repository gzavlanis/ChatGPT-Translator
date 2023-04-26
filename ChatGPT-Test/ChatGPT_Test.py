#### Take a look at readme file first ####

import openai
import streamlit as st
from PIL import Image

# image
image = Image.open('nn.png')

# model angine AND openai api key
model_engine = "text-davinci-003"
openai.api_key = "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"

# function to handle the translation
def translate_text(text, target_language):
    prompt = f"Translate '{text}' to {target_language}" # define the prompt for ChatGPT model
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 1024, n = 1, stop = None, temperature = 1.0) # generate translation
    translated_text = response.choices[0].text.strip() # extract translation
    return translated_text

def main():

    # building the frontend
    st.sidebar.header('Language Translation App')
    st.sidebar.write('A simple translation app that uses chatGPT api to translate text')
    st.sidebar.write('[About GPT Models](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer)')
    st.sidebar.write('Powered by [OpenAI](https://openai.com)')
    st.image(image)
    text_input = st.text_input('Enter the text you want to translate')
    target_language = st.selectbox('Select language of translation', ['Greek', 'English', 'French', 'Spanish', 'German'])
    translate_button = st.button('Translate text')
    translated_text = st.empty()
    if translate_button:
        translated_text.text('Translating...')
        translated_text.text(translate_text(text_input, target_language))
if __name__ == '__main__':
    main()


