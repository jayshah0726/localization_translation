import json

message_key = "phone_verification_success"

def load_translations(language_code):
    with open(f"translation_{language_code}.json", "r", encoding="utf-8") as file:
        return json.load(file)

def translate_message(translations, message_key, **kwargs):
    message_template = translations.get(message_key, "")
    return message_template.format(**kwargs)

# Load translations
translations_en = load_translations("en")
translations_hi = load_translations("hi")

# Dynamic content
phone_number = "1234567890"

# Get translated messages
message_en = translate_message(translations_en, message_key, phone_number=phone_number)
message_hi = translate_message(translations_hi, message_key, phone_number=phone_number)

print(message_en)
print(message_hi) 
