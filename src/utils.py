import hashlib

def hash_password(input_string: str) -> str:
    """
    Gera um hash SHA-256 para a string de entrada fornecida.

    Args:
        input_string (str): A string que será hasheada
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()