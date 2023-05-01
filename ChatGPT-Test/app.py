#### Take a look at readme file first ####

import openai
import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

# image
image = Image.open('nn.png')

# model angine
model_engine = "text-davinci-003"

style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
"""

# function to handle the translation
def translate_text_simple(text, target_language):
    prompt = f"Translate '{text}' to {target_language}" # define the prompt for ChatGPT model
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 1200, n = 1, stop = None, temperature = 0.4) # generate translation
    translated_text = response.choices[0].text.strip() # extract translation
    return translated_text

def translate_text_specific(text, target_language, text_type):
    prompt = f"Translate '{text}' to {target_language}. The text to be translated is a {text_type}"
    response = openai.Completion.create(engine = model_engine, prompt = prompt, max_tokens = 1200, n = 1, stop = None, temperature = 0.3) # generate translation
    translated_text = response.choices[0].text.strip() # extract translation
    return translated_text

def main():

    # building the frontend
    st.sidebar.image(image)
    st.sidebar.header('Language Translation App')
    st.sidebar.write('A simple translation app that uses chatGPT api to translate text')
    st.sidebar.write('[About GPT Models](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer)')
    openai.api_key = st.sidebar.text_input('Enter your OpenAI API key', key = "str") # user must enter openAI API key
    if st.sidebar.button("Refresh page"):
        st.cache_resource.clear()
    st.sidebar.write('Powered by [OpenAI](https://openai.com) and [Streamlit](https://streamlit.io)')
    
    text_input = st.text_input('Enter the text you want to translate or')
    uploaded_file = st.file_uploader("choose a file to import  data for translation")
    translate_data = st.button('Translate data')

    target_language = st.selectbox('Select language of translation', ['Greek', 'English', 'French', 'Spanish', 'German'])
    text_type = st.selectbox('Specify the kind of text you want to translate', ['', 'Poem', 'Song', 'Medical document', 'Financial report', 'Proverb', 'Athletic Team', 'Sport Championship'])
    translate_button = st.button('Translate text')
    translated_text = st.empty()
    st.markdown(style, unsafe_allow_html = True)

    if translate_button:
        translated_text.text('Translating...')
        if text_type == '':
            translated_text.text(translate_text_simple(text_input, target_language))
        else: translated_text.text(translate_text_specific(text_input, target_language, text_type))

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, index_col = "data") # row must always have header 'data'

        # translation process for data
        translations = np.array([])
        if translate_data:
            for i in df.index:
                translation = translate_text_simple(i, target_language)
                translations = np.append(translations, translation)
            translated_text.text(translations) # show all translations

if __name__ == '__main__':
    main()
