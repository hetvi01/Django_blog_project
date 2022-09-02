import polib
from googletrans import Translator

"""
This module modify django.po with translated msgid to appropriate msgstr
"""

# Hardcoded codes version.
langs = ['en', 'fr']
translator = Translator()

for lang_code in langs:
    po = polib.pofile(f'/media/root292/Data/django/django_project/locale/{lang_code}/LC_MESSAGES/django.po')

    for entry in po:
        if 'fuzzy' in entry.flags:
            entry.msgstr = ""
        if entry.msgstr == "":
            translation = translator.translate(entry.msgid, dest=lang_code)
            entry.msgstr = translation.text
    po.save()
