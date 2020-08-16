from pygments.lexers import get_all_lexers


ALL_LEXER_CHOICES = [(lexer[1][0], lexer[0]) for lexer in get_all_lexers()]
