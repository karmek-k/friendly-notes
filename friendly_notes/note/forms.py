from django import forms

from note.models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['date']
