from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PessoaForm, EnderecoForm
# Create your views here.


def pessoa(request):
    form = PessoaForm()
    if request.method == "POST":
        form = PessoaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pessoa foi salvo.')

            return redirect('pessoa')

    return render(request, 'core/pessoa.html', {'form': form})


def endereco(request):
    form = EnderecoForm()
    if request.method == "POST":
        form = EnderecoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Endereco foi salvo.')

            return redirect('endereco')

    return render(request, 'core/endereco.html', {'form': form})
