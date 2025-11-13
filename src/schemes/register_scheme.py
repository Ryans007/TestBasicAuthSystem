from typing import Optional
from pydantic import BaseModel

class UserRegisterSchema(BaseModel):
    """
    Esquema Pydantic para o registro de um novo usuário.
    Attributes:
        username (str): Nome de usuário único.
        email (str): Endereço de e-mail do usuário.
        full_name (Optional[str]): Nome completo do usuário.
        password (str): Senha do usuário.
    """
    username: str
    email: str
    full_name: Optional[str] = None
    password: str

