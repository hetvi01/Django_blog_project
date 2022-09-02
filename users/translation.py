from django.contrib.auth.models import User
from modeltranslation.translator import register, TranslationOptions

from users.models import Profile

"""
This module Translate Model
"""


# @register(User)
# class UserTranslationOptions(TranslationOptions):
#     fields = ('email', 'username')
#
#
# @register(Profile)
# class ProfileTranslationOptions(TranslationOptions):
#     fields = ('image',)
