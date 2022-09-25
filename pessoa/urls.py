from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListaPessoaView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView


urlpatterns = [
    path('', login_required(ListaPessoaView.as_view()), name='pessoa.index'),
    path('novo/', login_required(PessoaCreateView.as_view()), name='pessoa.novo'),
    path('<int:pk>/editar', login_required(PessoaUpdateView.as_view()), name='pessoa.editar'),
    path('<int:pk>/remover', login_required(PessoaDeleteView.as_view()), name='pessoa.remover')
]