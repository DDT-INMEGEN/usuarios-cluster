from django.db import models

class User(models.Model):
    uid = models.Autofield(primary_key = True)
    name = models.CharField(250, verbose_name = "Nombre completo")
    email = models.CharField(320, verbose_name = "Correo electrónico")
    group = models.ForeignKey('Group', verbose_name = "Grupo de investigación")
    phone = models.CharField(30, verbose_name = "Extensión o teléfono")
    is_employee = models.Boolean()
    expire_date = models.DateField(verbose_name = "¿Cuándo termina el proyecto/postgrado?")

class Group(models.Model):
    gid = models.AutoField(primary_key = True)
    nombre = models.CharField(500)
    responsable = models.ForeignKey('User')
