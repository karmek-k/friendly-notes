from random import randint

from django.views import generic
from django.shortcuts import redirect, render

from note.models import Note
from note.forms import NoteForm


class IndexView(generic.TemplateView):
    template_name = 'note/index.html'


class AddNoteView(generic.CreateView):
    form_class = NoteForm
    template_name = 'note/add_note.html'


class GetNoteView(generic.DetailView):
    model = Note
    template_name = 'note/get_note.html'


def random_note(request):
    note_count = Note.objects.count()

    if note_count:
        random_pk = randint(1, note_count)
        return redirect('note:get', pk=random_pk)

    return render(request, 'note/no_notes.html')
