#CT1: Registro com todos os campos corretos
def test_register_success(client):
    response = client.post(
        "/register",
        data={
            "username": "kevin",
            "email": "kevin@email.com",
            "password": "Abc#1234"
        }
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Usuário criado com sucesso"

#CT3: Email vazio
def test_register_email_vazio(client):
    response = client.post(
        "/register",
        data={
            "username": "joao",
            "email": "",
            "password": "Abc#1234"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email não pode estar vazio"

#CT4: Email sem '@'
def test_register_email_sem_arroba(client):
    response = client.post(
        "/register",
        data={
            "username": "joao",
            "email": "email_errado.com",
            "password": "Abc#1234"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email inválido"

#CT5: Email sem dominio
def test_register_email_sem_dominio(client):
    response = client.post(
        "/register",
        data={
            "username": "joao",
            "email": "email_errado@",
            "password": "Abc#1234"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email inválido"

#CT6: Senha menor que 8 caracteres
def test_register_senha_curta(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "abc"
        }
    )
    assert response.status_code == 400
    assert "Senha deve ter entre" in response.json()["detail"]

#CT7: Senha maior que 16 caracteres
def test_register_senha_longa(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "Abc#12345678901234"
        }
    )
    assert response.status_code == 400
    assert "Senha deve ter entre" in response.json()["detail"]

#CT8: Senha sem letra maiúscula
def test_register_senha_sem_maiuscula(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "abc#1234"
        }
    )
    assert response.status_code == 400
    assert "ao menos 1 letra maiúscula" in response.json()["detail"]

#CT9: Senha sem letra minúscula
def test_register_senha_sem_minuscula(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "ABC#1234"
        }
    )
    assert response.status_code == 400
    assert "ao menos 1 letra minúscula" in response.json()["detail"]

#CT10: Senha sem número
def test_register_senha_sem_numero(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "ABC#aaaa"
        }
    )
    assert response.status_code == 400
    assert "ao menos 1 número" in response.json()["detail"]

#CT11: Senha sem caractere especial permitido
def test_register_senha_sem_especial(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "Abc12345"
        }
    )
    assert response.status_code == 400
    assert "ao menos 1 caractere especial" in response.json()["detail"]

#CT12: Senha com caractere especial NÃO permitido (ex: @)
def test_register_senha_com_especial_n_permitido(client):
    response = client.post(
        "/register",
        data={
            "username": "maria",
            "email": "maria@email.com",
            "password": "Abc@1234"
        }
    )
    assert response.status_code == 400
    assert "Caractere especial inválido" in response.json()["detail"]

#CT13: Usuário já registrado
def test_register_usuario_duplicado(client):
    # cria primeiro
    client.post(
        "/register",
        data={
            "username": "userx",
            "email": "x@x.com",
            "password": "Abc#1234"
        }
    )

    # tenta criar de novo
    response = client.post(
        "/register",
        data={
            "username": "userx",
            "email": "x2@x.com",
            "password": "Abc#1234"
        }
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Usuário já existe"
