from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from MainApp.models import Snippet, LANGS
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from MainApp.forms import SnippetForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def snippets_list(request, user_id=None):
    snippets = Snippet.objects
    if user_id != None:
        snippets = snippets.filter(user__lte=user_id)
        context = {
            'pagename': 'Просмотр сниппетов',
            "user_id": user_id,
            'snippets': snippets
        }
    else:
        snippets = snippets.filter(public=1)
        context = {
            'pagename': 'Просмотр сниппетов',
            "user_id": 0,
            'snippets': snippets
        }
    return render(request, 'pages/snippets_view.html', context)


def snippet_detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = {
            'pagename': 'Детали сниппета',
            'snippet': snippet
        }
        return render(request, 'pages/snippet_detail.html', context)

    except ObjectDoesNotExist:
        return HttpResponseNotFound(
            f"""<p>Сниппет с id={snippet_id} не найден<br>
            <a href="/snippets/list">Назад к списку сниппетов</a></p>""")


def snippet_edit(request, snippet_id: int):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return Http404
    # Varian1
    # ===== Получение данных сниппета с помощью SnippetForm
    # if request.method == "GET":
    #     form = SnippetForm(instance=snippet)
    #     return render(request, "pages/snippet_add.html")

    # Varian 2
    # Хотим получить страницу с данными сниппета
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Редактирование сниппета',
            'snippet': snippet,
            'type': "edit"
        }
        # print("11111")
        return render(request, 'pages/snippet_detail.html', context)
    if request.method == "POST":
        # from pprint import pprint
        # pprint(vars(request))
        data_form = request.POST
        snippet.name = data_form["name"]
        snippet.lang = data_form["lang"]
        snippet.code = data_form["code"]
        try:
            print(data_form["public"])
            snippet.public=1
        except:
            snippet.public=0
        snippet.save()
        # print("22222")
        return redirect('snippets-list')


def snippet_add(request):
    # Создаем пустую форму при запросе методом GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/snippet_add.html', context)
    # Получаем данные из формы и на их основе создаем новый snippet в БД
    if request.method == "POST":
        # from pprint import pprint
        # pprint(vars(request))
        # pprint(request.POST)
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user=request.user
            snippet.save()
            return redirect("snippets-list") # GET /snippets/list
        return render(request, "pages/snippet_add.html", {'form': form})


def snippet_delete(request, snippet_id):
    snippet = get_object_or_404(Snippet, id = snippet_id)
    if request.method in ("GET","POST"):
        snippet.delete()
    return redirect('snippets-list')


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(request, username=username, password=password)
        print("username =", username)
        print("password =", password)
        print("is authenticated =", user.is_authenticated)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect("home")