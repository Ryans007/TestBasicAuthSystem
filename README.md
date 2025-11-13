### Como executar o projeto:
Para executar o projeto, siga os passos abaixo:
1. Clone o repositório:
   ```bash
    git clone <URL_DO_REPOSITORIO>
   ```
2. Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```
3. Vá para a pasta raiz e execute:
   ```bash
    cd src 
    uvicorn index:app --port 8001
    ```
   
### Para executar os testes:
Para executar os testes do projeto, siga após a instalação das dependências:
1. Vá para a pasta raiz do projeto:
   ```bash
   cd src
   ```
2. Execute o comando do PyTest:
   ```bash
   pytest -v
   ```

   