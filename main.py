from translator import Translator

# Initialize translators for different languages
translator_en = Translator('en')
translator_hi = Translator('hi')

# Dynamic content
phone_number = "1234567890"
name = "Raj"

# Translate messages
try:
    message_en = translator_en.translate("phone_verification_success", phone_number=phone_number)
    message_hi = translator_hi.translate("phone_verification_success", phone_number=phone_number)
    
    greeting_en = translator_en.translate("greeting_message", name=name)
    greeting_hi = translator_hi.translate("greeting_message", name=name)
    
    print(message_en) 
    print(message_hi) 
    print(greeting_en) 
    print(greeting_hi) 
except KeyError as e:
    print(e)
except Exception as e:
    print(e)
