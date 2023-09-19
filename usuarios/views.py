from rest_framework import viewsets
from rest_framework.response import Response
from usuarios.models import Usuario
from usuarios.serializers import UsuarioSerializer
from rest_framework.decorators import action


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() # Se trae todos los usuarios
    serializer_class = UsuarioSerializer

    @action(detail=True, methods=['POST'])
    def approve(self, request, pk=None):
        user = self.get_object()

        # Check if the requesting user is a superuser
        if not request.user.is_superuser:
            return Response({'detail': 'You do not have permission to approve users.'})

        # Approve the user
        user.user_is_approved = True
        user.save()

        return Response({'message': 'User approved successfully'})

class TestViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all() # Se trae todos los usuarios
    serializer_class = UsuarioSerializer

    def list(self, request, *args, **kwargs):
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

        return Response({"nice": 1})