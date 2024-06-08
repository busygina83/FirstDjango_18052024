from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from MainApp.forms import SnippetForm

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    form = SnippetForm()
    context = {
        'pagename': 'Добавление нового сниппета',
        'form': form
    }
    return render(request, 'pages/add_snippet.html', context)


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

def create_snippet(request):
    from pprint import pprint
    if request.method == "POST":
        pprint(vars(request))
        pprint(request.POST)
        form = SnippetForm(request.POST)
        if form.is_vslid():
            form.save()
            return redirect("snippets-list") # GET /snippets/list
        return render(request, "pages/add_snippet.html", {'form': form})