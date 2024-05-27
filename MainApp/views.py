from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

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

# python manage.py shell_plus --ipython
# item = Item(name="Кроссовки", brand="abibas", count=10)
# item.save()
# item = Item(name="Куртка кожаная", brand="Fin-Flare", count=2)
# item.save()
# item = Item(name="Напиток 1 литр", brand="Coca-cola", count=12)
# item.save()
# item = Item(name="Картофель фри", brand="MacDonalds", count=0)
# item.save()
# item = Item(name="Кепка", brand="Nike", count=124)
# item.save()

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

def item_details(request, item_id: id):
    for item in items:
        if item['id']==item_id:
            return render(request, "item.html", {"item": item})
        # item = next ((item for item in items if item['id'] == item_id), None)
    return HttpResponseNotFound(
        f"""<p>Товар с id={item_id} не найден<br>
        <a href="/items">Назад к списку товаров</a></p>""")