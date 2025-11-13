#CT2: Login com todos os campos corretos
def test_login_success(client):
    # criar usuário antes
    client.post(
        "/register",
        data={
            "username": "kevin",
            "email": "kevin@email.com",
            "password": "Abc#1234"
        }
    )

    response = client.post(
        "/login",
        data={"username": "kevin", "password": "Abc#1234", "email": "kevin@email.com"}
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Login efetuado com sucesso"

#CT14: Usuário não encontrado
def test_login_usuario_inexistente(client):
    response = client.post(
        "/login",
        data={"username": "naoexiste", "password": "Abc#1234", "email": "x@x.com"}
    )
    assert response.status_code == 401
    assert response.json()["detail"] == "Usuário não encontrado"

#CT15: Senha incorreta
def test_login_senha_incorreta(client):
    client.post(
        "/register",
        data={"username": "ana", "email": "ana@gmail.com", "password": "Abc#1234"}
    )

    response = client.post(
        "/login",
        data={"username": "ana", "password": "Errada123!", "email": "ana@gmail.com"}
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Senha incorreta"
