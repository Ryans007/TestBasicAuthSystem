from fastapi import APIRouter, Depends, HTTPException

from database_ import get_users_db

from models import UserModel
from schemes import UserRegisterSchema

from typing import Dict, Any

from validators.email_validate import is_a_valid_email
from validators.password_validate import validate_password
from utils import hash_password

router = APIRouter()

@router.post("/register", response_model=UserRegisterSchema)
async def register_user(user: UserRegisterSchema, db=Depends(get_users_db)) -> Dict[str, Any]:
    """Register a new user."""
    # Buscar usuário existente usando query do SQLAlchemy
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário ja existe no banco de dados.")

    if not is_a_valid_email(user.email):
        raise HTTPException(status_code=400, detail="Email inválido.")

    password_error = validate_password(user.password)
    if password_error is not None:
        raise HTTPException(status_code=400, detail=f"Senha inválida. {password_error}")

    # Criar novo usuário com senha hasheada
    hashed_pwd = hash_password(user.password)
    new_user = UserModel(
        username=user.username,
        email=user.email,
        full_name=user.full_name,
        hashed_password=hashed_pwd
    )

    # Adicionar e salvar no banco de dados
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return user



