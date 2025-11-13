"""Módulo para validação de endereços de e-mail."""
import re

def validate_email(email: str):
    if len(email) == 0:
        return 0

    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(padrao, email):
        return 1
    else:
        return -1
