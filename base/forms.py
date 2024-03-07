from django import forms
from .import models


class createarticle(forms.ModelForm):
    class Meta:
        model =models.Article
        fields = ['title', 'content', 'slug', 'thumb']