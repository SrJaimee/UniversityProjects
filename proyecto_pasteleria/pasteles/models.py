from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Pasteles(models.Model):
    nombre = models.CharField(
        max_length=200,
        unique=True,
        verbose_name="Nombre del Pastel"
    )
    descrepcion = models.TextField(
        blank=True,
        null=True,
        verbose_name="Descripcion del Pastel"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    precio = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Precio"
    )

class Meta:
    ordering = ['nombre']
    verbose_name = "Producto"
    verbose_name_plural = "Productos"
    
def __str__(self):
    return self.nombre