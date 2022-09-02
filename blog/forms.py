from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from blog.models import Post


class CretePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        labels = {
            'title': _('title'),
            'content': _('content'),
        }

