from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500,  null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True,  null=False, blank=False)
    password = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        db_table = 'usuario'
        verbose_name_plural = 'Tabla para registrar usuarios'
    
    def __str__(self):
        return self.id_usuario



class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, null=True, blank=True)
    descripcion = models.CharField(max_length=2000)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, to_field='id_usuario', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tarea'
        verbose_name_plural = 'Tabla para generar tareas de usuarios'

    def __str__(self):
        return self.id_tarea
    
