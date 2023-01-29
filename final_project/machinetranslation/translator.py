"""Translation Python Script."""
import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = "2018-05-01"

""" creating an instance of the IBM Watson Language translator """
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version = VERSION,authenticator = authenticator)
language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """fonction translate from english to frensh"""
    try:
        translation = language_translator.translate(
            text = english_text,model_id = 'en-fr').get_result()
        print(json.dumps(translation, indent=2, ensure_ascii=False))
        french_text = translation["translations"][0]["translation"]
    except ApiException as ex:
        french_text = ""
        print("Method failed with status code " +str(ex.code) + ": " + ex.message)
    return french_text

def french_to_english(french_text):
    """fonction translate from frensh to english"""
    try:
        translation = language_translator.translate(
            text=french_text, model_id='fr-en').get_result()
        print(json.dumps(translation, indent=2, ensure_ascii=False))
        english_text = translation["translations"][0]["translation"]
    except ApiException as ex:
        english_text = ""
        print("Method failed with status code " +str(ex.code) + ": " + ex.message)
    return english_text
