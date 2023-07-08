from django.urls import path
from .Views.UsuariosView import Usuarios


urlpatterns = [
    #URL users

    #users-list
    path('usuarios/', Usuarios.UsuarioList.as_view(), name='usuario-list'),
    #users-ge
    path("usuarios/<int:id>", Usuarios.UsuariosDetails.as_view(), name="usuarios-details"),
    #user-create
    path("usuarios/", Usuarios.UsuarioList.as_view(), name="usuarios-create")

    
]