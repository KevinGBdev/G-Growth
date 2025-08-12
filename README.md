# G-Growth

Minimal Django project bootstrapped for the G-Growth platform.

## Setup

Crie um arquivo de ambiente `.env` a partir de `.env.example` e ajuste as
credenciais do banco de dados e a chave secreta.

```bash
pip install -r requirements.txt  # ou instale Django e psycopg2-binary manualmente
python manage.py migrate
python manage.py runserver
```

## Como testar

Execute a verificação do projeto e os testes automatizados com:

```bash
python manage.py check
python manage.py test
```

Esses comandos ajudam a garantir que as configurações estão corretas. Se o banco
de dados não estiver configurado, as migrações e testes podem falhar.

## Apps

- **accounts** – basic authentication with an extended user profile.
- **diagnostico**, **ferramentas**, **erp_light**, **erp_pro**, **pagamentos** –
  placeholders for future development.
- **core_erp** – base models for ERP modules.
- **dashboard** – simple user dashboard.
- **integra** – control of enabled modules per user.
