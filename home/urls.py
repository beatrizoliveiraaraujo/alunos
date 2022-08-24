from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_home,
         name='index_home'
         ),
    path('cadastro_usuario/', views.cadastro_usuario,
         name='cadastro_usuario'
         ),
    path('login_usuario/', views.login_usuario,
         name='login_usuario'
         )
]
