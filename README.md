# Verbeux-Backend

Este é um projeto de uma API escrita com [Django](https://www.djangoproject.com/) e [Django REST Framework](https://www.django-rest-framework.org/) para criar e se atualizar sessões de um chatbot assistente, feita na plataforma [Verbeux](https://verbeux.com.br), que auxilia o cliente no recebimentos de feedbacks, como reclamações, elogios e sugestões. Além disso, a API é responsavel por gerenciar as entidades de feedback em um banco de dados SQLITE, permitindo realizar as operações CRUD (Create, Read, Update, Delete).

## Instalação

- Primeiro certifique-se que tem o python instalado globalmente no seu computador. Se não, você pode instala-lo por [aqui](https://www.python.org").
- Depois de fazer isso, confirme de que tem um ambiente virtual do python como o virtualenv instalado globalmente também. Se não, rode isso:
  ```bash
      $ pip install virtualenv
  ```
- Depois, clone esse repositório no seu PC:

  ```bash
      $ git clone https://github.com/Giryerume/verbeux-backend.git
  ```

- #### Dependências

  - Entre no diretório do repositório criado:
    ```bash
        $ cd verbeux-backend
    ```
  - Crie e ative o seu ambiente virtual:
    ```bash
        $ virtualenv venv -p python3
        $ source venv/bin/activate
    ```
  - Instale as dependências necessárias para rodar o projeto:
    ```bash
        $ pip install -r requirements.txt
    ```
  - Crie e execute as migrações:
    ```bash
        $ python manage.py makemigrations
        $ python manage.py migrate
    ```
  - Renomeie o arquivo `.env.example` para `.env`:
    ```bash
        $ cp env.example .env
    ```
  - Preencha os valores no arquivo .env com suas próprias chaves de API:

    ```
        API_PRIVATE_KEY=sua_chave_de_api_aqui
    ```

    ##### OBS: Por enquanto vai ser necessário solicitar uma chave de api válida por esse [formulário](https://forms.gle/QjG26SUzKjGdjU9j9)

- #### Iniciar
  Inicialize o servidor usando o comando:
  ```bash
      $ python manage.py runserver
  ```

## Uso

A API estará disponível em `http://localhost:8000/api`.

### Rotas

- `POST api/session`: Cria uma sessão com o assistente.
- `PUT api/session/<id>`: Atualiza a sessão com uma messagem
- `GET api/feedbacks`: Retorna todos os produtos.
- `GET api/feedbacks/<id>`: Retorna um feedback específico pelo ID.
- `POST api/feedbacks`: Cria um novo feedback.
- `PUT api/feedbacks/<id>`: Atualiza um feedback existente pelo ID.
- `DELETE api/feedbacks/<id>`: Exclui um feedback existente pelo ID.

## Contribuição

Contribuições são bem-vindas! Se você encontrar um problema ou tiver uma sugestão, por favor, abra uma issue ou envie um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
