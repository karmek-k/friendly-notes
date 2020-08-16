from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

from note.lexer_choices import ALL_LEXER_CHOICES


class Note(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('title')
    )
    content = models.TextField(verbose_name=_('content'))
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('date')
    )
    language = models.CharField(
        choices=ALL_LEXER_CHOICES,
        max_length=21,
        blank=True,
        verbose_name=_('language')
    )

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note:get', kwargs={'pk': self.pk})
