from rest_framework import routers
from usuarios.views import UsuarioViewSet, TestViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('a', TestViewSet.as_view({'get': 'list'}))
    # path('approve_user/', UsuarioViewSet.as_view({'post': 'approve'}))
]

urlpatterns += [
    path('usuarios/<int:pk>/approve/', UsuarioViewSet.as_view({'post': 'approve'}), name='approve_user'),
]