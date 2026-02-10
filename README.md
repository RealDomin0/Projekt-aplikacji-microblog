# Projekt aplikacji webowej typu microblog
## Opis projektu
Microblog to aplikacja webowa stworzona z wykorzystaniem frameworka *Django*, umożliwiająca użytkownikom tworzenie, edytowanie oraz usuwanie krótkich postów. Aplikacja posiada system rejestracji i logowania użytkowników, profile użytkowników oraz prosty feed z postami.

Aplikacja jest przeznaczona dla każdego użytkownika chcącego publikować krótkie treści.

---

## Funkcjonalności
- rejestracja i logowanie użytkowników,
- edycja danych użytkownika oraz profilu,
- tworzenie postów,
- edycja i usuwanie **tylko własnych postów**,
- feed z listą postów,
- walidacja pustych postów,
- wyszukiwarka postów,
- flaga `is_owner` określająca właściciela posta,
- ochrona widoków przed nieautoryzowanym dostępem.

---

## Struktura projektu
```
microblog
├─ account
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  ├─ models.py
│  ├─ signals.py
│  ├─ static
│  │  └─ css
│  │     └─ base.css
│  ├─ templates
│  │  ├─ account
│  │  │  ├─ edit_profile.html
│  │  │  ├─ home.html
│  │  │  ├─ login.html
│  │  │  ├─ profile_detail.html
│  │  │  ├─ register.html
│  │  │  └─ register_done.html
│  │  ├─ base.html
│  │  └─ registration
│  │     ├─ logged_out.html
│  │     └─ login.html
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ __init__.py
│  └─ __pycache__
├─ manage.py
├─ media
│  └─ users
│     └─ default
│        └─ avatar.jpg
├─ microblog
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  ├─ __init__.py
│  └─ __pycache__
└─ posts
   ├─ admin.py
   ├─ apps.py
   ├─ forms.py
   ├─ migrations
   ├─ models.py
   ├─ templates
   │  └─ posts
   │     ├─ feed.html
   │     ├─ post_create.html
   │     ├─ post_delete.html
   │     └─ post_edit.html
   ├─ tests.py
   ├─ urls.py
   ├─ views.py
   ├─ __init__.py
```

---

## Technologie 
- Python
- Django
- HTML5
- CSS3
- MySQL
- GitHub

---

## Uruchomienie projektu
1. Sklonuj repozytorium:
```
git clone https://github.com/RealDomin0/microblog.git
```
2. Przejdź do katalogu projektu:
```
cd microblog
```
3. Utwórz i aktywuj środowisko wirtualne:
```
python -m venv venv
source venv/bin/activate
```
4. Zainstaluj zależności:
```
pip install -r requirements.txt
```
5. Wykonaj migracje:
```
python manage.py migrate
```
6. Uruchom serwer:
```
python manage.py runserver
```
