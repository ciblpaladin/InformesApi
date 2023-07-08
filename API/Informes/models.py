from django.db import models
# Create your models here

class Estado(models.Model):

    estado_estado = models.CharField(max_length=20)


class Rol(models.Model):

    nombre_rol = models.CharField(max_length=20)

class Usuario(models.Model):

    nombre_usuario = models.CharField(max_length=20)
    apellido_usuario = models.CharField(max_length=20)
    cedula_usuario = models.CharField(max_length=20)
    celular_usuario = models.CharField(max_length=20)
    correo_usuario = models.EmailField()
    rol_fk = models.ForeignKey(Rol, on_delete=models.CASCADE)
    estado_usuario = models.ForeignKey(Estado, on_delete=models.CASCADE)
    password = models.CharField(max_length=200, default=0)

    foreings = {
        "rol_fk" : Rol,
        "estado_usuario": Estado
    }
    

class Regional(models.Model):

    regional_regional = models.CharField(max_length=20)
    

class Especialidad(models.Model):

    nombre_especialidad = models.CharField(max_length=20)

class Prestador(models.Model):

    nombre_prestador = models.CharField(max_length=20)

class Perfil(models.Model):

    nombre_perfil = models.CharField(max_length=20)

class TipoAccion(models.Model):

    nombre_tipo_accion = models.CharField(max_length=20)

class AdminContratacion(models.Model):

    nombre_admin_contratacion = models.CharField(max_length=20)
    apellido_admin_contratacion = models.CharField(max_length=20)
    celular_admin_contratacion = models.CharField(max_length=20)
    correo_admin_contratacion = models.CharField(max_length=20)

class InformeModificacionUsuarios(models.Model):

    nombre_profesional = models.CharField(max_length=20)
    documento_profesional = models.CharField(max_length=20)
    numero_caso_profesional = models.CharField(max_length=20)
    accion_fk = models.ForeignKey(TipoAccion, on_delete=models.CASCADE)
    fecha_informe = models.DateField()
    regional_fk = models.ForeignKey(Regional, on_delete=models.CASCADE)
    especialidad_fk = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    prestador_fk = models.ForeignKey(Prestador, on_delete=models.CASCADE)
    perfil_fk = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    admin_fk = models.ForeignKey(AdminContratacion, on_delete=models.CASCADE)

class Estado_casos(models.Model):

    estado_caso = models.CharField(max_length=20)

class InformeRegistroCasos(models.Model):

    numero_caso = models.CharField(max_length=20)
    hora_registro_caso = models.DateTimeField()
    hora_finalizacion_caso = models.DateTimeField()
    estado_gestion_cfk = models.ForeignKey(Estado_casos, on_delete=models.CASCADE)
    analista_asignado_fk  = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    foreings = {
        "estado_gestion_cfk" : Estado_casos,
        "analista_asignado_fk": Usuario
    }  

