from django.shortcuts import render, redirect
from crud.forms import EquipeForm
from crud.models import equipe

# Create your views here.
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
    data = {}
    data['db'] = equipe.objects.get(pk=pk).delete()
    return redirect('home')