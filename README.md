# Django Blog

A simple multi-user blog built with Django: sign up, log in, write posts, and browse them with pagination.

Originally built in 2020 while learning Django; updated in 2026.

## Tech stack

- Python 3.10+ / Django 5.2 LTS
- Class-based views (`ListView`, `DetailView`, `CreateView`) with `LoginRequiredMixin`
- Django auth (registration, login, logout)
- SQLite, Bootstrap 4 templates

## Features

- User registration that logs the new user in
- Login / logout
- Create blog posts (author is set to the logged-in user)
- Home page with newest posts first, 3 per page
- Post detail page

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd django_projects/blog
python manage.py migrate
python manage.py createsuperuser   # optional, for /admin
python manage.py runserver          # http://127.0.0.1:8000
```

Settings are read from environment variables (see [`.env.example`](.env.example)). With the defaults, the app runs in local development mode.

Run the tests:

```bash
python manage.py test
```

## 2026 update

- Django 3.0 → 5.2 LTS; added `requirements.txt`
- `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS` now come from environment variables (the old key was committed to the repo and is no longer used)
- Logout now uses a POST form (Django 5 no longer allows logging out via GET)
- Nav shows Log In / Create Account or Post Now / Log Out depending on login state
- Fixed a broken stylesheet path, a stray closing `</div>`, and the register page heading
- Added tests for auth, post creation and pagination
- Stopped tracking `db.sqlite3` and `__pycache__`; added `.gitignore`
