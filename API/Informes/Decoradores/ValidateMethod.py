
from ..models import Usuario, Rol, Estado
from django.db import models
import bcrypt

def transform_post_data_to_model(foreings: dict):
    def transform(func):
        def wrapper( *args, **kwargs):
            
            request = args[1]
            models = {}
            foreings_keys = {}
                
            for key, model in foreings.items():
                    foreings_keys[key] = lambda id: model.objects.get(id=id)
                     
            if request.method == "POST":
                for key, valor in request.POST.items():
                    if key != "csrfmiddlewaretoken" and  key !=  "password_confirm":
                        if key in foreings_keys:
                            models[key] = foreings_keys[key](valor)
                            
                        else:
                            
                            models[key] = valor
            
            request.model = models  

            return func(*args, **kwargs)
        return wrapper
    return transform
   

def Update_user(func):
    def action(*args, **kwargs):

        
        usuario = Usuario.objects.get(id= kwargs["id"])
        request = args[1]
        foreing_keys = {

            "rol_fk" : lambda id: Rol.objects.get(id=id),
            "estado_usuario": lambda id: Estado.objects.get(id=id)

        }
        if usuario:

            for key, value in request.POST.items():
                if key != "csrfmiddlewaretoken":
                    
                    if key in foreing_keys:
                        
                        setattr(usuario, key, foreing_keys[key](value))
                    else:
                        setattr(usuario,key,value)

        request.usuario = usuario
        return func(*args, **kwargs)            

    return action   