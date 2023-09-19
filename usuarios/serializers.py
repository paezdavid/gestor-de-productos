from rest_framework import serializers, request
from usuarios.models import Usuario



# Se guarda el usuario registrado aca
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'username', 'password', 'user_is_approved']

    def save(self, commit=True):
        print(request)

        serializer = UsuarioSerializer(data=request)
        if serializer.is_valid():
            serializer.save()



        # Save the provided password in hashed format
        user = super().save()
        user.set_password(self.validated_data["password"])
        if commit:
            user.save()
        return user