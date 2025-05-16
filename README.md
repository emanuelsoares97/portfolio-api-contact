# Portfolio API - Contact

API desenvolvida com Flask para receber mensagens de formulário de contato e enviá-las por e-mail. Ideal para integrar em portfólios ou websites pessoais.

## Tecnologias utilizadas

- **Python 3**
- **Flask**
- **smtplib** para envio de e-mails
- **dotenv** para gerenciamento de variáveis de ambiente

## Funcionalidades

- Recebe dados de formulário via requisição POST
- Envia as informações recebidas por e-mail para um endereço configurado

## Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/emanuelsoares97/portfolio-api-contact.git
cd portfolio-api-contact
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
EMAIL_FROM=seu_email@gmail.com
EMAIL_TO=destinatario_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_aplicativo
```

> **Nota:** Para contas Gmail, é necessário criar uma senha de aplicativo. Consulte a documentação do Gmail para mais informações.

### 5. Execute a aplicação

```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## Endpoint

- **POST** `/`  
  Envia uma nova mensagem de contato.  
  **Corpo da requisição (JSON):**
  ```json
  {
    "name": "Seu Nome",
    "email": "seuemail@example.com",
    "message": "Sua mensagem aqui"
  }
  ```

## Segurança

Certifique-se de não expor suas credenciais de e-mail. Utilize variáveis de ambiente e nunca faça commit do arquivo `.env`.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por [Emanuel Soares](https://github.com/emanuelsoares97)
