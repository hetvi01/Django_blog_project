from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Profile

from modeltranslation.forms import TranslationModelForm


class UserRegisterForm(UserCreationForm, TranslationModelForm):
    email = forms.EmailField(label=_('email'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(TranslationModelForm):
    email = forms.EmailField(label=_('email'))

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(TranslationModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        lables = {
            'image': _('image'),
            'Choose file': _('Choose file'),
            'No file chosen': _('No file chosen')

        }

