import django_filters
from django.utils.translation import gettext_lazy as _
from modeltranslation.forms import TranslationModelForm

from .models import *


class PostFilter(django_filters.FilterSet):
    """
    To filter blog using blog title or blog author name
    """
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'author']

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['title'].label = _('title')
        self.filters['author'].label = _("author")


