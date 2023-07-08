from typing import Any
from rest_framework import generics
from rest_framework.response import Response
from ..Servicios.ModelsCrud import ModelsCrud
from ..models import Usuario, Rol,Estado
from ..Serializers.Serializers import UsuarioSerializer
from ..Decoradores.ValidateMethod import transform_post_data_to_model
import json

class Usuarios:

    class UsuarioList(generics.CreateAPIView):
        
        def __init__(self, **kwargs: Any) -> None:

            self.usuarios_crud = ModelsCrud.create_model_crud(model=Usuario)

        def get(self,request) -> Response:

            usuarios = self.usuarios_crud.all()
            serializer = UsuarioSerializer(usuarios, many=True)

            return Response(serializer.data)
        
        @transform_post_data_to_model(Usuario.foreings)
        def post(self, request)-> Response:
            print(request.model)
            usuario_Crear = self.usuarios_crud.create(request.model)
            return Response({"mensaje":"Usuario creado"})

        

    class UsuariosDetails(generics.RetrieveAPIView):

        def __init__(self, **kwargs: Any) -> None:

            self.usuarios_crud = ModelsCrud.create_model_crud(model=Usuario)

        def get(self, request, id : int) ->Response:

            usuario = self.usuarios_crud.get(id=id) 
            serializer = UsuarioSerializer(usuario)
            return Response(serializer.data)   
    

