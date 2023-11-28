from django.db import models
 
# Create your models here.

class Asignatura(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "Asignaturas"
    def __str__(self):
        return f"{self.name}"   
    
class Licencia(models.Model):
    date = models.DateField()
    aceptada= models.BooleanField()
    imagen = models.ImageField(upload_to='licencias/') 
    class Meta:
        verbose_name_plural = "Licencias"
    def __str__(self):
        return f"{self.date}"   

class Teacher(models.Model):
    name= models.CharField(max_length=500)
    asignatura = models.ManyToManyField(Asignatura)
    rut = models.CharField(max_length=10, unique=True)
    dias_presente = models.IntegerField(max_length=100, null=True,default=0 )
    dias_ausente= models.IntegerField(max_length=100, null=True, default=0)
    licencia = models.ForeignKey(Licencia, null=True, blank=True, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Profesores"
    def __str__(self):
        return f"{self.name}"   

