from django.db import models

# Create your models here.
class Eats(models.Model):
    id_eat = models.AutoField(primary_key=True)
    name = models.CharField( verbose_name="Nombre restaurant",max_length=50)
    mainImage = models.ImageField(verbose_name="Imagen Portada", upload_to='restaurants',blank=True, null=True)
    image1 = models.ImageField(verbose_name="Imagen 1", upload_to='restaurants',blank=True, null=True,)
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to='restaurants',blank=True, null=True,)
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to='restaurants',blank=True, null=True,)
    address = models.CharField(verbose_name="Dirección", max_length=50)
    description = models.TextField(verbose_name="descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"
        ordering = ['-created']

    def __str__(self):
        return self.name
