from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

def list_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas.html', {'pessoas':pessoas})

def create_pessoas(request):
    form = PessoaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_pessoas')
        
    return render(request, 'pessoas-form.html', {'form':form})

def update_pessoas(request, id):
    pessoa = Pessoa.objects.get(id=id)
    form = PessoaForm(request.POST or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('list_pessoas')

    return render(request, 'pessoas-form.html', {'form':form, 'pessoa':pessoa})

def delete_pessoas(request, id):
    pessoa = Pessoa.objects.get(id=id)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('list_pessoas')

    return render(request, 'pessoa-delete-confirm.html', {'pessoa':pessoa})
