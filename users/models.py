from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key = True)
    name = models.CharField("Nombre completo", max_length = 250)
    email = models.EmailField("Correo electrónico", max_length = 320)
    phone = models.CharField("Extensión o teléfono", max_length = 30)
    is_employee = models.BooleanField("¿Es empleado?")
    expire_date = models.DateField("¿Cuándo termina el proyecto/postgrado?")
    grupos = models.ManyToManyField(verbose_name = "Grupo de investigación", to = "Group")

class Group(models.Model):
    gid = models.AutoField(primary_key = True)
    nombre = models.CharField("Grupo de Investigación", max_length = 500)
    responsable = models.ForeignKey(verbose_name = "Investigador Líder", to = "User")
