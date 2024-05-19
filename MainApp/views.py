from django.shortcuts import render # type: ignore
from django.http import HttpResponse, HttpResponseNotFound # type: ignore

author = {
    "familyname": "Бусыгина",
    "name": "Инна",
    "surname": "Владимировна",
    "telephone": "8-888-888-88-88",
    "email": "busygina83@mail.ru"}

items = [
    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
    {"id": 7, "name": "Картофель фри" ,"quantity":0},
    {"id": 8, "name": "Кепка" ,"quantity":124}
]

def home(request):
    fio="Бусыгина И.В."
    text = f"""
        <h1>"Изучаем django"</h1>
        <strong>Автор</strong>: <i>{fio}</i>
        """
    return HttpResponse(text)

def about(request):
    text = f"""<p>
        Имя: <strong>{author['familyname']}</strong><br>
        Отчество: <strong>{author['name']}</strong><br>
        Фамилия: <strong>{author['surname']}</strong><br>
        телефон: <strong>{author['telephone']}</strong><br>
        email: <strong>{author['email']}</strong><br>
        </p>"""
    return HttpResponse(text)

def item_list(request):
    text = "<strong>Список товаров:</strong><br>"
    for item in items:
        text += f"""<p>
            {item['id']}: {item['name']}
            <a href="/item/{item['id']}"> подробнее...</a>
            </p>"""
    return HttpResponse(text)

def item_detail(request, id):
    text = ""
    print (f"{id=}")
    for item in items:
        if item['id']==id:
            text = f"""<p>
                id: <strong>{item['id']}</strong><br>
                name: <strong>{item['name']}</strong><br>
                quantity: <strong>{item['quantity']}</strong><br>
                <a href="/items">назад к списку товаров</a><br>
                </p>"""
            return HttpResponse(text)
    if text == "":
        text = f"<p>Товар с id={id} не найден</p>"
        return HttpResponseNotFound(text)