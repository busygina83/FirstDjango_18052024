from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    fio="Бусыгина И.В."
    text = f"""
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>{fio}</i>
    """
    return HttpResponse(text)

def about(request):
    familyname="Бусыгина"
    name="Инна"
    surname="Владимировна"
    telephone="8-888-888-88-88"
    email="busygina83@mail.ru"
    text = f"""<p>
    Имя: <strong>{familyname}</strong><br>
    Отчество: <strong>{name}</strong><br>
    Фамилия: <strong>{surname}</strong><br>
    телефон: <strong>{telephone}</strong><br>
    email: <strong>{email}</strong><br>
    </p>"""
    return HttpResponse(text)