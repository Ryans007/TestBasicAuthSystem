from fastapi import APIRouter, Depends, HTTPException, Form
from database_ import get_users_db
from models.user import UserModel
from utils import hash_password
from validators.email_validate import  validate_email
from validators.password_validate import  validate_pass
router = APIRouter()

@router.post("/register")
# Mude a assinatura desta função
async def register_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(""),
    db=Depends(get_users_db)
):
    # 1. Verifica se já existe
    user_exist = db.query(UserModel).filter(UserModel.username == username).first()
    if user_exist:
        raise HTTPException(400, "Usuário já existe")

    # 2. Validar e-mail
    v_email = validate_email(email)
    if v_email == 0:
        raise HTTPException(status_code=400, detail="Email não pode estar vazio")
    elif v_email == -1:
        raise HTTPException(status_code=400, detail="Email inválido")

    # 3. Validar senha
    v_pass = validate_pass(password)
    match v_pass:
        case 0:
            raise HTTPException(status_code=400, detail="Senha deve ter entre 8 e 16 caracteres")
        case -1:
            raise HTTPException(status_code=400, detail="Senha deve conter ao menos 1 letra maiúscula")
        case -2:
            raise HTTPException(status_code=400, detail="Senha deve conter ao menos 1 letra minúscula")
        case -3:
            raise HTTPException(status_code=400, detail="Senha deve conter ao menos 1 número")
        case -4:
            raise HTTPException(status_code=400, detail="Caractere especial inválido")
        case -5:
            raise HTTPException(status_code=400, detail="Senha deve conter ao menos 1 caractere especial")

    # Salva
    new_user = UserModel(
        username=username,
        email=email,
        hashed_password=hash_password(password)  # <-- Correção!
    )

    db.add(new_user)
    db.commit()

    return {"message": "Usuário criado com sucesso"}
