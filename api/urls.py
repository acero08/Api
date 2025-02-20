from django.urls import path
from .views import get_Categoria

urlpatterns = [

    path('categoria/', get_Categoria, name='get_categoria'),
]
