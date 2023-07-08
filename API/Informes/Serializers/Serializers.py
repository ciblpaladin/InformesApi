from rest_framework import serializers
from ..models import Usuario, Rol, Estado

class Estadoserializer(serializers.ModelSerializer):
    class Meta:

        model = Estado
        fields = "__all__"

class Rolserializer(serializers.ModelSerializer):
    class Meta:

        model = Rol
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    rol_fk = Rolserializer()
    estado_usuario = Estadoserializer()
    
    class Meta:

        model = Usuario
        fields = "__all__"
        depth = 1   