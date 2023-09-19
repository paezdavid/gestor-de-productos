from rest_framework import serializers
from rest_framework.response import Response
from productos.models import Producto, Categoria, Imagen

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre']


class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ["url"]


class ProductoDetallesSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)
    imagenes = ImagenSerializer(many=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'estado', 'categorias', 'imagenes']

    def update(self, instance, validated_data):
        # Update the 'nombre' and 'estado' fields
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.estado = validated_data.get('estado', instance.estado)

        # Update the nested fields 'categorias' and 'imagenes'
        categorias_data = validated_data.get('categorias')
        if categorias_data is not None:
            # Remove the existing associations with categories
            instance.categorias.clear()
            for categoria_data in categorias_data:
                # Create new Categoria objects if they don't exist
                categoria, created = Categoria.objects.get_or_create(nombre=categoria_data['nombre'])
                instance.categorias.add(categoria)

        imagenes_data = validated_data.get('imagenes')
        if imagenes_data:
            # Remove the existing associations with images
            instance.imagenes.all().delete()
            for imagen_data in imagenes_data:
                Imagen.objects.create(producto=instance, **imagen_data)

        instance.save()
        return instance
        

class ProductoDetallesUnauthenticatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'estado']


