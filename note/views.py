from django.views import generic
from django.urls import reverse_lazy

from note.models import Note
from note.forms import NoteForm


class IndexView(generic.TemplateView):
    template_name = 'note/index.html'


class AddNoteView(generic.CreateView):
    form_class = NoteForm
    template_name = 'note/add_note.html'
    # success_url = reverse_lazy('note:get')


class GetNoteView(generic.DetailView):
    model = Note
    template_name = 'note/get_note.html'
