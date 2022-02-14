from django.shortcuts import render, redirect
from crud.forms import EquipeForm, ServicosForm, PostsForm
from crud.models import equipe, servicos, posts

# Create your views here.

### Equipe views
def home(request):
    return render(request, 'index.html')

def equipe_home(request):
    data = {}
    data['db'] = equipe.objects.all()
    return render(request, 'equipe.html', data)

def form(request):
    data = {}
    data['form'] = EquipeForm()
    return render(request, 'form.html', data)

def create(request):
    form = EquipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('equipe_home')

def view(request, pk):
    data = {}
    data['db'] = equipe.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = equipe.objects.get(pk=pk)
    data['form'] = EquipeForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = equipe.objects.get(pk=pk)
    form = EquipeForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = equipe.objects.get(pk=pk)
    db.delete()
    return redirect('home')

## Serviços

def servicos_home(request):
    data = {}
    data['db'] = servicos.objects.all()
    return render(request, 'servicos.html', data)

def servicos_form(request):
    data = {}
    data['form'] = ServicosForm()
    return render(request, 'servicos_form.html', data)

def servicos_create(request):
    form = ServicosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servicos_home')

def servicos_view(request, pk):
    data = {}
    data['db'] = servicos.objects.get(pk=pk)
    return render(request, 'servicos_view.html', data)

def servicos_edit(request, pk):
    data = {}
    data['db'] = servicos.objects.get(pk=pk)
    data['form'] = ServicosForm(instance=data['db'])
    return render(request, 'servicos_form.html', data)

def servicos_update(request, pk):
    data = {}
    data['db'] = servicos.objects.get(pk=pk)
    form = ServicosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('servicos_home')

def servicos_delete(request, pk):
    db = servicos.objects.get(pk=pk)
    db.delete()
    return redirect('servicos_home')

## Postagem

def posts_home(request):
    data = {}
    data['db'] = posts.objects.all()
    return render(request, 'posts.html', data)


def posts_form(request):
    data = {}
    data['form'] = PostsForm()
    return render(request, 'posts_form.html', data)

def posts_create(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('posts_home')

def posts_view(request, pk):
    data = {}
    data['db'] = posts.objects.get(pk=pk)
    return render(request, 'posts_view.html', data)

def posts_edit(request, pk):
    data = {}
    data['db'] = posts.objects.get(pk=pk)
    data['form'] = PostsForm(instance=data['db'])
    return render(request, 'posts_form.html', data)

def posts_update(request, pk):
    data = {}
    data['db'] = posts.objects.get(pk=pk)
    form = PostsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('posts_home')

def posts_delete(request, pk):
    db = posts.objects.get(pk=pk)
    db.delete()
    return redirect('posts_home')