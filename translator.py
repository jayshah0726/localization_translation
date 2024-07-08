import json
import os

class Translator:
    def __init__(self, language_code):
        self.translations = self.load_translations(language_code)
    
    def load_translations(self, language_code):
        file_path = f"translation_{language_code}.json"
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Translation file for language '{language_code}' not found.")
    
    def translate(self, message_key, **kwargs):
        message_template = self.translations.get(message_key, "")
        if not message_template:
            raise KeyError(f"Message key '{message_key}' not found in translations.")
        return message_template.format(**kwargs)
