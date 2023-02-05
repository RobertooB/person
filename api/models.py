from django.db import models
    
class Catalogo (models.Model):
    nombre_catalogo = models.CharField(max_length=80)
    valor = models.CharField(max_length=50) 
    
class Institucion (models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    actividad = models.CharField(max_length=100) 

class Persona (models.Model):
    nombres = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    cedula = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)  
    direccion = models.CharField(max_length=100)
    convencional = models.CharField(max_length=7)
    celular = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    aceptado = models.BooleanField(blank=True)
    sexo = models.ForeignKey(Catalogo,on_delete=models.PROTECT)
    institucion = models.ForeignKey(Institucion,on_delete=models.PROTECT)
    tipo = models.ForeignKey(Catalogo, on_delete=models.PROTECT, related_name= "fk_catalogo")
    etnia = models.ForeignKey(Catalogo, on_delete=models.PROTECT, related_name= "fk_catalogoEtnia", blank= True)


    