# G-Growth

Minimal Django project bootstrapped for the G-Growth platform.

## Setup

Create an environment file `.env` based on `.env.example` and adjust the
database credentials and secret key.

```bash
pip install -r requirements.txt  # or install Django and psycopg2-binary manually
python manage.py migrate
python manage.py runserver
```

## Apps

- **accounts** – basic authentication with an extended user profile.
- **diagnostico**, **ferramentas**, **erp_light**, **erp_pro**, **pagamentos** –
  placeholders for future development.
- **core_erp** – base models for ERP modules.
- **dashboard** – simple user dashboard.
- **integra** – control of enabled modules per user.
