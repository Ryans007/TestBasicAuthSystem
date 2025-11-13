"""Módulo para validação de endereços de e-mail."""

def is_a_valid_email(email: str) -> bool:
    """
    Valida o formato do endereço de e-mail fornecido.

    Args:
        email (str): O endereço de e-mail a ser validado.

    Returns:
        bool: True se o e-mail for válido, False caso contrário.
    """
    email_patterns = ("@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@icloud.com")

    # Verificar se contém @ e se termina com um dos domínios válidos
    if "@" not in email:
        return False

    for pattern in email_patterns:
        if email.endswith(pattern):
            return True

    return False
