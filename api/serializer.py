from rest_framework import serializers
from .models import Categoria, Ingrediente, Receta, RecetaIngrediente, Menu


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'


class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'


class RecetaIngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetaIngrediente
        fields = '__all__'


class MenuSerializer(serializers.ModelSerializer):
    recetas = RecetaSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'
