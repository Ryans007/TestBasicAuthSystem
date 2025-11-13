from typing import Optional
from pydantic import BaseModel

class UserLoginSchema(BaseModel):
    """
    Esquema Pydantic para o login de um usuário.
    Attributes:
        username (str): Nome de usuário do usuário.
        password (str): Senha do usuário.
    """
    username: str
    password: str

