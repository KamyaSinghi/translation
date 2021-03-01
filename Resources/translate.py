from flask import request
from flask_restful import Resource, Api, abort
from googletrans import Translator
import goslate
import logging
from app import *
from app.resources import *
from utils.response_body import response_body

supported_languages = {
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'cy': 'Welsh',
    'pt': 'Portuguese',
    'zh-CN': 'Chinese Simplified',
    'zh-TW': 'Chinese Traditional'
}
log = logging.getLogger(__name__)
gs = goslate.Goslate()
translator = Translator()

class TextTranslation(Resource):
    def detect(self):
        json_data = request.get_json(force=True)
        text = json_data.get('text')

        if not text:
            """  abort(401, error='Text is required') """
            err_msg = 'text is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400

        source_language_id = gs.detect(text)
        source_language_name = gs.get_languages()[source_language_id]

        if source_language_id:
            if source_language_id not in supported_languages:
                err_msg = 'this language is not supported'
                logging.error(err_msg)
                return response_body(None, err_msg + getSupportedLanguage()), 400

        return response_body({'source_language_name': source_language_name}, message='successfully detected'), 200

    def Conversion_googleapi(self):
        """
            Dynamically translate text. Supported language set {en, zh-CN, zh-TW, hi, fr, es, cy, pt}
        """
        json_data = request.get_json(force=True)
        source = json_data.get('source')
        destination = json_data.get('destination')
        text = json_data.get('text')

        if not source:
            err_msg = 'source language code is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400
        if not destination:
            err_msg = 'destination language code is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400
        if not text:
            err_msg = 'text is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400
        if source:
            if source not in supported_languages:
                err_msg = 'please select a supported source language code'
                logging.error(err_msg)
                return response_body(None, err_msg + getSupportedLanguage()), 400
        if destination:
            if destination not in supported_languages:
                err_msg = 'please select a supported destination language code'
                logging.error(err_msg)
                return response_body(None, err_msg + + getSupportedLanguage()), 400

        t = translator.translate(text, src=source, dest=destination)
        """
        print("Destination Text : " + t.text)
        
        """
        return response_body({
            'source': source + ' - ' + supported_languages[source],
            'destination': destination + ' - ' + supported_languages[destination],
            'translated_text': t.text},
            'translated_text successfully'), 201

    """
        return response_body({'converted text': t.text}, message='Successfully converted'), 200
        """


    def Coversion_goslate(self):
        json_data = request.get_json(force=True)
        destination = json_data.get('destination')
        text = json_data.get('text')

        if not destination:
            err_msg = 'destination language code is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400
        if not text:
            err_msg = 'text is required'
            logging.error(err_msg)
            return response_body(None, err_msg), 400
        if destination:
            if destination not in supported_languages:
                err_msg = 'please select a supported destination language code'
                logging.error(err_msg)
                return response_body(None, err_msg + + getSupportedLanguage()), 400
        dest_text = gs.translate(text, destination)
        return response_body({'converted text': dest_text}, message='successfully converted'), 200




def getSupportedLanguage():
    res = ""
    for x in supported_languages:
        res = res + (x+':'+supported_languages[x])+" , "
    return res

