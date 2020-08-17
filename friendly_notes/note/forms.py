from django import forms
from captcha.fields import CaptchaField

from note.models import Note


class NoteForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Note
        exclude = ['date']
