from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pessoa
from .forms import PessoaForm

class ListaPessoaView(ListView):
    model = Pessoa
    queryset = Pessoa.objects.all().order_by('nome_completo')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('nome') or None

        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)
            
        return queryset
    
    
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class PessoaUpdateView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    success_url = '/pessoa/'

class PessoaDeleteView(DeleteView):
    model = Pessoa
    success_url = '/pessoa/'