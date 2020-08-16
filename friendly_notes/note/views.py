from random import choice

from django.views import generic
from django.urls import reverse
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
    pk_list = Note.objects.all().values_list('pk', flat=True)

    if pk_list:
        random_pk = choice(pk_list)
        return redirect('note:get', pk=random_pk)

    url = reverse('note:add')
    return render(request, 'note/no_notes.html', {'url': url})
