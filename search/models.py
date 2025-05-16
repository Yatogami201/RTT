from django.db import models    

class Search(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.JSONField(default=list)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='posts/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)