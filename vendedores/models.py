from django.db import models
from django.contrib.auth.models import User  # para asociar publicaciones con el usuario

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones')
    imagen = models.ImageField(upload_to='publicaciones/', blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.vendedor.username}"



