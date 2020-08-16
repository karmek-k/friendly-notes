from django.db import models

from note.lexer_choices import ALL_LEXER_CHOICES


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        choices=ALL_LEXER_CHOICES,
        max_length=21,
        blank=True
    )

    def __str__(self):
        return self.title
