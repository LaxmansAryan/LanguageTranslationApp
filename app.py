import streamlit as st
import numpy as np

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, authenticator

api_key = 'jKCI1mRitv74PBwYUx96w2MJPbBVB15qtm6AEj4GLg6M'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/e19fba10-a1d8-44ae-b818-c6f558fc856b'


authenticator = IAMAuthenticator(apikey=api_key)

langtranslator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator
)

langtranslator.set_service_url(url)

st.title("Language-Translator")
st.subheader("Made by Aryan S. Sawant")

option = st.selectbox(
    'Which language would you choose to type',
    ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))

option1 = st.selectbox(
    'Which language would you like to translate to',
    ('English', 'Arabic', 'Hindi', 'German', 'Spanish', 'Korean'))

sent = "Enter the text in "+option+" language in the text-area provide below"


language_lib = {'English': 'en', 'Arabic': 'ar',
                'Hindi': 'hi', 'Spanish': 'es', 'German': 'de', 'Korean': 'ko'}

sentence = st.text_area(sent, height=250)

if st.button("Translate"):
    try:
        if option == option1:
            st.write("Select different language for translation")

        else:
            translate_code  = language_lib[option]+'-'+language_lib[option1]

            translation = langtranslator.translate(
                text=sentence, model_id=translate_code)
            
            ans = translation.get_result()['translations'][0]['translation']

            sent1 = 'Translated text in '+option1+' language is shown below'

            st.markdown(sent1)
            st.write(ans)

    except:
        st.write("Please do cross check if text-area is filled with sentences or not.")
