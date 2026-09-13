from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('<int:id>/', views.detalle_nota, name='detalle_nota'),
]