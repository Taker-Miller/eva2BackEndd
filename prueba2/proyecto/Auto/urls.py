from django.urls import path
from . import views

urlpatterns = [
    path('auto/', views.lista_auto, name='lista_auto'),
    path('<int:pk>/', views.detalle_auto, name='detalle_auto'),
    path('auto/agregar/', views.agregar_auto, name='agregar_auto'),
    path('<int:pk>/editar/', views.editar_auto, name='editar_auto'),
    path('<int:pk>/eliminar/', views.eliminar_auto, name='eliminar_auto'),
    path('', views.home_view, name='home'),
]
