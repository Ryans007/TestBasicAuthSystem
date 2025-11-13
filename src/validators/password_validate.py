"""Módulo para validação de senhas."""

def validate_password(password: str) -> str | None:
    """
    Valida se a senha fornecida atende aos critérios de segurança.

    Args:
        password (str): A senha a ser validada.

    Returns:
        str | None: Mensagem de erro se a senha for inválida, None caso contrário.
    """
    especial_caracters = "&*$%#!^~[]"

    if len(password) < 8 or len(password) > 16:
        return "A string de senha deve ter entre 8 e 16 caracteres."

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_special_caracter = any(char in especial_caracters for char in password)

    if not has_upper:
        return "A string de senha deve conter ao menos uma letra maiúscula."
    if not has_lower:
        return "A string de senha deve conter ao menos uma letra minúscula."
    if not has_number:
        return "A string de senha deve conter ao menos um número."
    if not has_special_caracter:
        return "A string de senha deve conter ao menos um caractere especial."
    return None
