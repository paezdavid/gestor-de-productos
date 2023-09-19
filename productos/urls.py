from rest_framework import routers
from productos.views import ProductoViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]