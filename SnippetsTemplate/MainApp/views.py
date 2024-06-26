from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from MainApp.models import Snippet, LANGS
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound, HttpResponseNotAllowed
from MainApp.forms import SnippetForm, UserRegistrationForm, CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


# @login_required(login_url="home")
def snippets_list(request, user_id=None):
    snippets = Snippet.objects
    if user_id != None:
        # snippets = snippets.filter(user__lte=user_id)
        snippets = snippets.filter(user=request.user)
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
    return render(request, 'pages/snippets_list.html', context)


def snippet_detail(request, snippet_id):
    context = {
        'pagename': 'Детали сниппета',
    }
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(
            f"""<p>Сниппет с id={snippet_id} не найден<br>
            <a href="/snippets/list">Назад к списку сниппетов</a></p>""")
    else:
        context["snippet"] = snippet
        context["type"] = "view"
        return render(request, "pages/snippet_detail.html", context)


@login_required(login_url="home")
def snippet_add(request):
    # Создаем пустую форму при запросе методом GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/snippet_add.html', context)
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            if request.user.is_authenticated:
                snippet.user=request.user
            snippet.save()
            return redirect("snippets-list")
        return render(request, "pages/snippet_add.html", {'form': form})


@login_required(login_url="home")
def snippet_edit(request, snippet_id: int):
    try:
        snippet = Snippet.objects.filter(user=request.user).get(id=snippet_id)
    except ObjectDoesNotExist:
        return Http404
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


@login_required(login_url="home")
def snippet_delete(request, snippet_id):
    snippet = get_object_or_404(Snippet.objects.filter(user=request.user), id = snippet_id)
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
            context = {
                "pagename": "PythonBin",
                "errors": ['wrong username or password']
            }
            return render(request, "pages/index.html", context)
    return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect("home")


def user_add(request):
    context = {
        'pagename': 'Регистрация нового пользователя'
    }
    if request.method == "GET":
        form = UserRegistrationForm()
        context['form'] = form
        return render(request, 'pages/registration.html', context)
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        context['form'] = form
        return render(request, "pages/registration.html", context)


@login_required
def comment_add(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(111)
        # if comment_form.is_valid():
        comment = form.save(commit=False)
        snippet_id = request.POST.get("snippet_id")
        snippet = Snippet.objects.get(id=snippet_id)
        comment.author = request.user
        comment.snippet = snippet
        comment.save()
        print(222)
        return redirect("snippet-detail", snippet_id=snippet.id)
        print(333)
    print(444)
    return HttpResponseNotAllowed(['POST'])