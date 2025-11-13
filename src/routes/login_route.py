from fastapi import APIRouter, Depends, HTTPException, Form

from database_ import get_users_db
from models.user import UserModel
router = APIRouter()

@router.post("/login")
# Mude a assinatura desta função
async def login_user(
    username: str = Form(...),
    password: str = Form(...),
    email: str = Form(...),
    db=Depends(get_users_db)
):
    """
    Realiza o login validando:
    - Usuário existente
    """


    # 1. Verificar usuário
    user = db.query(UserModel).filter(UserModel.username == username).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    # 2. Verificar senha
    if not user.verify_password(password):
        raise HTTPException(status_code=401, detail="Senha incorreta")

    # 3. Sucesso
    return {"message": "Login efetuado com sucesso", "username": user.username}
