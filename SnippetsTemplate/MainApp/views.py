from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from MainApp.forms import SnippetForm
from django.contrib import auth


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)

def snippet_add(request):
    # Создаем пустую форму при запросе методом GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    # Получаем данные из формы и на их основе создаем новый snippet в БД
    if request.method == "POST":
        from pprint import pprint
        pprint(vars(request))
        pprint(request.POST)
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authentificated:
                snippet.user=request.user
                snippet_add.save()
            return redirect("snippets-list") # GET /snippets/list
        return render(request, "pages/add_snippet.html", {'form': form})

def snippet_delete(request, snippet_id):
    snippet = get_object_or_404(Snippet, id = snippet_id)
    if request.method in ("GET","POST"):
        snippet.delete()
    return redirect('snippets-list')

def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {
        'pagename': 'Просмотр сниппетов',
        'snippets': snippets
    }
    return render(request, 'pages/view_snippets.html', context)

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
    context = {"pagename": "Редактирование сниппета"}
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return Http404
    # Varian1
    # ===== Получение данных сниппета с помощью SnippetForm
    # if request.method == "GET":
    #     form = SnippetForm(instance=snippet)
    #     return render(request, "pages/add_snippet.html")

    # Varian 2
    # Хотим получить страницу с данными сниппета
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'snippet': snippet,
            'type': "edit"
        }
        return render(request, 'pages/snipped_detail.html', context)
    
    if request.method == "POST":
        data_form = request.POST
        snippet.name = data_form["name"]
        snippet.code = data_form["code"]
        snippet.save()
        return redirect('snippets-list')
    
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username =", username)
        print("password =", password)
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            # Return error message
            pass

def logout(request):
    auth.logout(request)
    return redirect("home")