from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Categoria, Ingrediente, Receta, RecetaIngrediente, Menu
from .serializer import (
    CategoriaSerializer,
    IngredienteSerializer,
    RecetaSerializer,
    RecetaIngredienteSerializer,
    MenuSerializer
)

# CATEGORIA


@api_view(['GET', 'POST'])
def categoria_list(request):
    if request.method == 'GET':
        # Obtiene todas las categorías
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# INGREDIENTE


@api_view(['GET', 'POST'])
def ingrediente_list(request):
    if request.method == 'GET':
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ingrediente_detail(request, pk):
    ingrediente = get_object_or_404(Ingrediente, pk=pk)
    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RECETA


@api_view(['GET', 'POST'])
def receta_list(request):
    if request.method == 'GET':
        recetas = Receta.objects.all()
        serializer = RecetaSerializer(recetas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecetaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def receta_detail(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    if request.method == 'GET':
        serializer = RecetaSerializer(receta)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecetaSerializer(receta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        receta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# RECETA INGREDIENTE


@api_view(['GET', 'POST'])
def receta_ingrediente_list(request):
    if request.method == 'GET':
        receta_ingredientes = RecetaIngrediente.objects.all()
        serializer = RecetaIngredienteSerializer(
            receta_ingredientes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = RecetaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def receta_ingrediente_detail(request, pk):
    receta_ingrediente = get_object_or_404(RecetaIngrediente, pk=pk)
    if request.method == 'GET':
        serializer = RecetaIngredienteSerializer(receta_ingrediente)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RecetaIngredienteSerializer(
            receta_ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        receta_ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# MENU


@api_view(['GET', 'POST'])
def menu_list(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
