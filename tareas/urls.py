from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('<int:id>/', views.detalle_tarea, name='detalle_tarea'),
]