from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    # categorias = models.CharField(max_length=100)
    categorias = models.ManyToManyField(Categoria)

class Imagen(models.Model):
    url = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default="", related_name="imagenes")


    def __str__(self):
        return self.url


