import uvicorn
from fastapi import FastAPI

from routes.login_route import router as login_router
from routes.register_route import router as register_router

from database_ import AuthBase, auth_engine

app = FastAPI()

@app.on_event("startup")
def startup_event():
    """Cria as tabelas do banco de dados na inicialização do aplicativo."""
    try:
        print("Criando Banco de dados...")
        AuthBase.metadata.create_all(bind=auth_engine)
        print("Banco de dados criado com sucesso.")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")


@app.get("/")
def read_root():
    return {"message": "API de autenticação está funcionando! Coloque /docs no final da URL para acessar a documentação interativa."}

app.include_router(register_router, prefix="/auth", tags=["auth"])
app.include_router(login_router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)