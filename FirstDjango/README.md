# FirstDjango_18052024

## Инструкция по развертыванию проекта
1. `su - user; cd ~/Projects/FirstDjango`
2. `python3 -m venv django_venv`
3. `source django_venv/bin/activate`
4. `pip install -r requirements.txt`
5. `python manage.py migrate`
6. `python manage.py runserver`

## Запуск `ipython` в контексте приложения Django
```
python manage.py shell_plus --ipython
```

## Выгрузить данные из БД
```
python manage.py dumpdata MainApp --indent 4 > ./fixtures/items.json
```
## Загрузить данные в БД
```
python manage.py loaddata MainApp --indent 4 > ./fixtures/items.json
```

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