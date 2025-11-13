from sqlalchemy import Column, Integer, String

from typing import Optional
from pydantic import BaseModel

from database_ import AuthBase
from utils import hash_password

class UserModel(AuthBase):
    """
    Modelo que representa um usuário no banco de dados.
    Attributes:
        id (int): Identificador único do usuário.
        username (str): Nome de usuário único.
        email (str): Endereço de e-mail do usuário.
        full_name (Optional[str]): Nome completo do usuário.
        hashed_password (str): Senha do usuário armazenada de forma segura.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)

    def search_user_by_username(self, username: str) -> Optional['UserModel']:
        """Busca um usuário pelo nome de usuário."""
        return self.query.filter_by(username=username).first()

    def verify_password(self, password: str) -> bool:
        """
        Verifica se a senha fornecida corresponde ao hash armazenado.

        Args:
            password (str): A senha em texto plano para verificar

        Returns:
            bool: True se a senha corresponder ao hash, False caso contrário
        """
        return hash_password(password) == self.hashed_password

    def save_user(self, username: str, email: str, full_name: Optional[str], password: str) -> None:
        """Salva um novo usuário no banco de dados."""
        hashed_password = hash_password(password)

        new_user = UserModel(
            username=username,
            email=email,
            full_name=full_name,
            hashed_password=hashed_password
        )
        self.session.add(new_user)
        self.session.commit()

    def __repr__(self) -> str:
        return f"UserModel(id={self.id}, username='{self.username}', email='{self.email}', full_name='{self.full_name}')"