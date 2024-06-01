from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Item

author = {
    "familyname": "Бусыгина",
    "name": "Инна",
    "surname": "Владимировна",
    "telephone": "8-888-888-88-88",
    "email": "busygina83@mail.ru"}

# items = [
#     {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#     {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#     {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#     {"id": 7, "name": "Картофель фри" ,"quantity":0},
#     {"id": 8, "name": "Кепка" ,"quantity":124}
# ]

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
# python3 manage.py makemigrations
# # python3 manage.py migrate MainApp
# item_db = Item.objects.get(id=1)
# item_db.note="Очень крутые кроссы"
# item_db.save()
# item_db = Item.objects.get(id=2)
# item_db.note="Кепка летняя белая"
# item_db.save()
# item_db = Item.objects.get(id=3)
# item_db.note="Готовится в течении 5 минут"
# item_db.save()
# item_db = Item.objects.get(id=4)
# item_db.note="Есть газированный и негазированный"
# item_db.save()
# item_db = Item.objects.get(id=5)
# item_db.note="Смотрится стильно"
# item_db.save()

def home(request):
    context = {
        "name": "Бусыгина Инна Владимировна",
        "email": "busygina83@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html", {"about": author})

def item_list(request):
    items_db = Item.objects.all()
    return render(request, "items.html", {"items": items_db})

def item_details(request, item_id: id):
    # item = next ((item for item in items if item['id'] == item_id), None)
    try:
        item_db = Item.objects.get(id=item_id)
        return render(request, "item.html", {"item": item_db})
    except:
        return HttpResponseNotFound(
            f"""<p>Товар с id={item_id} не найден<br>
            <a href="/items">Назад к списку товаров</a></p>""")