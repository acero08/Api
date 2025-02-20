from django.shortcuts import render
from .models import Categoria, Ingrediente, Receta, RecetaIngrediente, Menu
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategoriaSerializer, IngredienteSerializer, RecetaSerializer, RecetaIngredienteSerializer, MenuSerializer


@api_view(['GET'])
def get_Categoria(request):
    return Response(CategoriaSerializer({'nombre': "entradas"}).data)
