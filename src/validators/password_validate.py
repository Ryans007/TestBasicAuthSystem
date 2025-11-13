"""Módulo para validação de senhas."""

def validate_pass(senha: str):
    if not (8 <= len(senha) <= 16):
        return 0

    tem_maiuscula = any(c.isupper() for c in senha)
    if not tem_maiuscula:
        return -1

    tem_minuscula = any(c.islower() for c in senha)
    if not tem_minuscula:
        return -2

    tem_numero = any(c.isdigit() for c in senha)
    if not tem_numero:
        return -3


    # Verifica se é um caractere especial inválido
    especiais_validos = "&*$%#!^~[]"
    for c in senha:
        if (c not in especiais_validos) and (not c.isalnum()):
            return -4

    tem_especial = any(c in especiais_validos for c in senha)
    if not tem_especial:
        return -5



    return 1
