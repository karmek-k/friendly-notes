from django.views import generic

from note.models import Note


class IndexView(generic.TemplateView):
    template_name = 'note/index.html'


class AddNoteView(generic.CreateView):
    model = Note
    template_name = 'note/add_note.html'
    fields = ['title', 'content', 'language']
