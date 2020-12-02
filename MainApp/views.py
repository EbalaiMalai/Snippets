from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.contrib import auth


def get_base_context(request, pagename):
    return {
        'pagename': pagename
    }
def thanks(request):
    context = get_base_context(request, 'Thanks!!!')
    return render(request, 'pages/thanks.html', context)

def index_page(request):
    context = get_base_context(request, 'PythonBin')
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm()
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)
    elif request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                snippet = form.save(commit=False)
                snippet.user = request.user
                snippet.save()
            return redirect('/thanks')
        context = get_base_context(request, 'Добавление нового сниппета')
        form = SnippetForm(request.POST)
        print("errors = ", form.errors)
        context["form"] = form
        return render(request, 'pages/add_snippet.html', context)



def snippets_page(request):
    context = get_base_context(request, 'Просмотр сниппетов')
    snippets = Snippet.objects.all()
    context["snippets"] = snippets
    # print("context = ", context)
    return render(request, 'pages/view_snippets.html', context)

def snippet(request, snippet_id):
    context = get_base_context(request, 'Страница сниппета')
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except Snippet.DoesNotExist:
        raise  Http404
    
    context["snippet"] = snippet
    return render(request, 'pages/snippet.html', context)


def login_page(request):
    context = get_base_context(request, "Авторизация")
    return render(request, 'pages/login.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # print(username, password)
        user = auth.authenticate(request, username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')

        errors = ["Некоректные данные", ]   
        context = get_base_context(request, "Авторизация")
        context['errors'] = errors
        context['username'] = username
        return render(request, 'pages/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/login/')