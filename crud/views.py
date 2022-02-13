from django.shortcuts import render, redirect
from crud.forms import EquipeForm, ServicosForm
from crud.models import equipe, servicos

# Create your views here.

### Equipe views
def home(request):
    data = {}
    data['db'] = equipe.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = EquipeForm()
    return render(request, 'form.html', data)

def create(request):
    form = EquipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

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