# from tkinter import getboolean
from django.forms import ModelForm, ValidationError, TextInput, Textarea, CheckboxInput
from MainApp.models import Snippet

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'public']
        labels = {"name": "", "lang": "", "code": ""}
        widgets = {
            "name": TextInput(attrs={"placeholder": "Название сниппета"}),
            "code": Textarea(attrs={"placeholder": "Код сниппета"}),
            "public": CheckboxInput(attrs={"placeholder": "Публичный"})
        }

    def clean_name(self):
        snippet_name = self.cleaned_data.get("name")
        if len(snippet_name) > 3:
            return snippet_name
        raise ValidationError("snippet name too short")