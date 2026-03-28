🛍 ERD - Интернет-магазин одежды (Django + HTMX + Alpine.js)
🌟 Особенности проекта
Современный стек: Django + HTMX + Alpine.js
Две платежные системы: Stripe и Heleket (крипто)
Docker-контейнеризация с PostgreSQL
Кастомизированная модель пользователя
Защищенные настройки (CSRF, HTTPS, Security Headers)
🚀 Запуск проекта
1. Локальный запуск (без Docker)
Установите зависимости:
python -m pip install -r requirements.txt
Создайте и активируйте виртуальное окружение:
python -m venv venv        
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
Настройте переменные окружения:
# Заполните .env своими значениями(пример .env ниже)
Запустите миграции:
python manage.py migrate
Создайте суперпользователя:
python manage.py createsuperuser
Запустите сервер:
python manage.py runserver
2. Запуск на сервере (с SSL)
Подготовьте домен:

Укажите DNS запись для domen.com на ваш IP
Настройте .env:

SECRET_KEY='example'

POSTGRES_DB=enfdb
POSTGRES_USER=enfdb
POSTGRES_PASSWORD=enfdb
POSTGRES_HOST=localhost # db если запускаете на vps
POSTGRES_PORT=5432

STRIPE_SECRET_KEY='example'
STRIPE_WEBHOOK_SECRET='example'

HELEKET_API_KEY='example'
HELEKET_SECRET_KEY='example'
Получите сертификаты (certbot):
sudo certbot --nginx -d domen.com -d www.domen.com
Соберите контейнер:
docker-compose up --build -d
Соберите статику:
docker-compose exec web python manage.py collectstatic --no-input
🔒 Настройки безопасности
Проект предварительно настроен с:

CSRF защитой
Secure cookies
Security Headers
HTTPS при работе через Docker
🌍 Доступ к сайту
Локально: http://localhost:8000
В Docker с SSL: https://domen.com
⚙️ Важные настройки из settings.py
# Безопасность
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        # ... другие параметры
    }
}

# Платежные системы
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
HELEKET_API_KEY = os.getenv('HELEKET_API_KEY')

📐 ERD и скриншоты
- Поместите диаграмму ERD в `docs/erd.png` и скриншоты UI в `docs/screenshots/`.
- Пример встраивания в README:
  - ERD: `![ERD](docs/erd.png)`
  - Скриншот: `![Главная](docs/screenshots/home.png)`

🧹 Линтинг и код‑стайл
- Используется Ruff. Запуск локально:

```bash
ruff check .
```

🧪 Тесты
- Минимальные Django‑тесты добавлены. Запуск:

```bash
python manage.py test --verbosity 2
```

🤖 CI
- GitHub Actions запускает Ruff и Django‑тесты на PR/пушах (`.github/workflows/ci.yml`).