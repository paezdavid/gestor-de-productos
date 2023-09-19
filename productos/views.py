from rest_framework import viewsets, filters, serializers
from productos.models import Producto, Categoria, Imagen
from productos.serializers import ProductoDetallesSerializer, ProductoDetallesUnauthenticatedSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .permissions import IsApprovedUser

# Create your views here.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetallesSerializer  

    # Filtrado de registros segun nombre, estado o categoria
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'estado', 'categorias__nombre']
    
    # Dependiendo de la autenticacion del usuario, retorna un serializer u otro
    def get_serializer_class(self):
        # if self.request.user.is_authenticated:
        #     # Retornar serializer para usuarios autenticados
        #     return ProductoDetallesSerializer
        if self.request.user.user_is_approved:
            # Retornar serializer para usuarios aprobados
            return ProductoDetallesSerializer
        else:
            # Retornar serializer para usuarios NO aprobados
            return ProductoDetallesUnauthenticatedSerializer

    

    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        
        # Crear un producto con los datos que vienen en la request
        instancia_de_producto = Producto.objects.create(nombre=request.data.get('nombre'), estado=request.data.get('estado'))

        # Por cada categoria que se haya enviado en la request, crear un objeto Categoria y anhadirlo al producto
        for categoria in request.data.get('categorias'):
            # instancia_de_categorias, created = Categoria.objects.filter(nombre=categoria['nombre'])
            # instancia_de_producto.categorias.add(instancia_de_categorias)

            # Attempt to get the Categoria object with the given nombre
            instancia_de_categorias = Categoria.objects.filter(nombre=categoria['nombre']).first()

            # Check if it exists, and if not, create a new Categoria
            if not instancia_de_categorias:
                instancia_de_categorias = Categoria.objects.create(nombre=categoria['nombre'])

            # Now you can add the Categoria to the producto
            instancia_de_producto.categorias.add(instancia_de_categorias)
            
        # Guardar el producto ya con las categorias anhadidas
        instancia_de_producto.save()


        # Por cada imagen (plain text url) que se haya enviado en la request, crear un objeto Imagen y anhadirlo al producto
        for imagen in request.data.get('imagenes'):
            instancia_de_imagenes = Imagen.objects.create(url=imagen['url'], producto=instancia_de_producto)
            instancia_de_imagenes.save()
    

        
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(instancia_de_producto)

        return Response(serializer.data)
    
