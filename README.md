# FirstDjango_18052024

## Инструкция по развертыванию проекта
1. `su - user; cd ~/Projects/FirstDjango`
2. `python3 -m venv django_venv`
3. `source django_venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py runserver`

## Дополнительно
1. Полезное дополнение для шаблонов `Django`
```
ext install batisteo.vscode-django
```

Добавить в `settings.json`
```
"emmet.includeLanguages": {
      "django-html": "html",
    },
"files.associations": {
      "*.html": "django-html"
    }
```