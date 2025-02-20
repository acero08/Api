from django.db import models

# Modelo para categorías de recetas


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre})"


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    unidad_medida = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.unidad_medida})"


class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='recetas')
    descripcion = models.TextField()
    instrucciones = models.TextField()
    # Número de personas que sirve la receta
    porciones = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.nombre})"


class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(
        Receta, on_delete=models.CASCADE, related_name='ingredientes')
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} {self.ingrediente} {self.cantidad}"


class Menu(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()  # Fecha del menú
    recetas = models.ManyToManyField(Receta, related_name='menus')

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"
