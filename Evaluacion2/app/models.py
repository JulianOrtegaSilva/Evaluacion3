from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.TextField()
    fecha_nacimiento = models.DateField()
    telefono= models.TextField()
    correo_electronico= models.EmailField()
    contrasena= models.CharField(max_length=50)

    def __str__(self):
        return self.rut

    
