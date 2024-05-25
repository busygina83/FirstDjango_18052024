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
    context = {
        "name": "Бусыгина Инна Владимировна",
        "email": "busygina83@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html", {"about": author})

def item_list(request):
    return render(request, "items.html", {"items": items})

def item_details(request, item_id):
    for item in items:
        if item['id']==item_id:
            return render(request, "item.html", {"item": item})
        # item = next ((item for item in items if item['id'] == item_id), None)
    return HttpResponseNotFound(
        f"""<p>Товар с id={item_id} не найден<br>
        <a href="/items">Назад к списку товаров</a></p>""")