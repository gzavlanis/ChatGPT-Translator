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
def translate_text_simple(text, target_language):
    prompt = f"Translate '{text}' to {target_language}" # define the prompt for ChatGPT model
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 1024, n = 0.7, stop = None, temperature = 1.0) # generate translation
    translated_text = response.choices[0].text.strip() # extract translation
    return translated_text

def translate_text_specific(text, target_language, text_type):
    prompt = f"Translate '{text}' to {target_language}. The text to be translated is a {text_type}"
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 1024, n = 0.7, stop = None, temperature = 1.0) # generate translation
    translated_text = response.choices[0].text.strip() # extract translation

def main():

    # building the frontend
    st.sidebar.header('Language Translation App')
    st.sidebar.write('A simple translation app that uses chatGPT api to translate text')
    st.sidebar.write('[About GPT Models](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer)')
    st.sidebar.write('Powered by [OpenAI](https://openai.com)')
    st.image(image)
    text_input = st.text_input('Enter the text you want to translate')
    target_language = st.selectbox('Select language of translation', ['Greek', 'English', 'French', 'Spanish', 'German'])
    text_type = st.selectbox('Specify the kind of text you want to translate', ['', 'Poem', 'Song', 'Medical document', 'Financial report', 'Proverb'])
    translate_button = st.button('Translate text')
    translated_text = st.empty()
    if translate_button:
        translated_text.text('Translating...')
        if text_type == '':
            translated_text.text(translate_text_simple(text_input, target_language))
        else: translated_text.text(translate_text_specific(text_input, target_language, text_type))
if __name__ == '__main__':
    main()


