from django.urls import path
from . import views

urlpatterns = [

    # Rutas para Categoria
    path('categorias/', views.categoria_list, name='categoria_list'),
    path('categorias/<int:pk>/', views.categoria_detail, name='categoria_detail'),

    # Rutas para Receta
    path('recetas/', views.receta_list, name='receta_list'),
    path('recetas/<int:pk>/', views.receta_detail, name='receta_detail'),

    # Rutas para RecetaIngrediente
    path('receta-ingredientes/', views.receta_ingrediente_list,
         name='receta_ingrediente_list'),
    path('receta-ingredientes/<int:pk>/', views.receta_ingrediente_detail,
         name='receta_ingrediente_detail'),

    # Rutas para Menu
    path('menus/', views.menu_list, name='menu_list'),
    path('menus/<int:pk>/', views.menu_detail, name='menu_detail'),
]
