from django import forms
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from .models import *


class AddPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Category not chose'

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean__title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('The title is longer than 200 characters.')
        return title
