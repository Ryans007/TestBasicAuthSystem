from fastapi import APIRouter, Depends, HTTPException

from database_ import get_users_db
from models.user import UserModel

router = APIRouter()

@router.post("/login")
async def login_user(username: str, password: str, db=Depends(get_users_db)):
    """Faz o login de um usuário existente."""
    user = db.query(UserModel).filter(UserModel.username == username).first()

    if not user or not user.verify_password(password):
        raise HTTPException(status_code=401, detail="Nome de usuário ou senha inválidos.")

    return {"message": "Login bem-sucedido", "username": user.username}