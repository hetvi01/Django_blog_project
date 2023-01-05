import json
import os

import polib
from dotenv import load_dotenv, find_dotenv
from googletrans import Translator

"""
This module modify django.po with translated msgid to appropriate msgstr
This is not recommended because it may contain fuzzy translation  but we can do it
"""
load_dotenv(find_dotenv())

# Example: SUPPORTED_LANGUAGES =['en', 'fr']
supported_langs= os.getenv('SUPPORTED_LANGUAGES')
#Example: PATH_TO_PO_FILE ='/media/django_project/locale/{lang_code}/LC_MESSAGES/django.po'
path_of_po_file=os.getenv('PATH_TO_PO_FILE')

#Translation Script for all language
translator = Translator()
for lang_code in json.loads(supported_langs):
    #read the po file
    po = polib.pofile(path_of_po_file.format(lang_code=lang_code))
    #iterate through each and every entry of po file
    for entry in po:
        #Avoid fuzzy translation which done automatically when we run makemessage command
        if 'fuzzy' in entry.flags:
            entry.msgstr = ""
        if entry.msgstr == "":
            # googletrans library translate entry.msgid to given language
            translation = translator.translate(entry.msgid, dest=lang_code)
            entry.msgstr = translation.text
    po.save()
print("Translation Done")
