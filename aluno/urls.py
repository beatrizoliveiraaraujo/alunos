from django.urls import path
from . import views

urlpatterns = [
    path('homealuno/',
         views.index_aluno,
         name='index_aluno'
         ),
    path('cadastro_aluno/',
         views.cadastro_aluno,
         name='cadastro_aluno'
         )
]
