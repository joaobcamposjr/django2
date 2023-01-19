from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelsForm
from .models import Produto
from django.shortcuts import redirect


# Create your views here.
def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_email()
            messages.success(request, 'E-mail envidao com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar e-mail!')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto salvo com sucesso!')
                form = ProdutoModelsForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelsForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')