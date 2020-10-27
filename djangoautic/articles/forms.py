from django import forms
from . import models
from django.utils.translation import gettext_lazy as _


class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug','thumb']


class CreateComment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
        labels = {
            'body': _('Place your comment')
        }
