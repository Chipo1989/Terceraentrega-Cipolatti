from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarea_list, name='tarea_list'),
    path('crear-tarea/', views.tarea_create, name='tarea_create'),
    path('crear-desarrollo/', views.desarrollo_create, name='desarrollo_create'),
    path('crear-estado/', views.estado_create, name='estado_create'),
    path('buscar/', views.tarea_search, name='tarea_search'),
]