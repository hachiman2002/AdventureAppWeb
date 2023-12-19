from django.db import models

# Create your models here.
class Destinations(models.Model):
    id_destination = models.AutoField(primary_key=True)
    name = models.CharField( verbose_name="Nombre Destino",max_length=50)
    mainImage = models.ImageField(verbose_name="Imagen Portada", upload_to='destinations',blank=True, null=True)
    image1 = models.ImageField(verbose_name="Imagen 1", upload_to='destinations',blank=True, null=True,)
    image2 = models.ImageField(verbose_name="Imagen 2", upload_to='destinations',blank=True, null=True,)
    image3 = models.ImageField(verbose_name="Imagen 3", upload_to='destinations',blank=True, null=True,)
    image4 = models.ImageField(verbose_name="Imagen 4", upload_to='destinations',blank=True, null=True,)
    image5 = models.ImageField(verbose_name="Imagen 5", upload_to='destinations',blank=True, null=True,)
    distance = models.IntegerField(verbose_name="Distancia de Curacautín (Kilometros)")
    suitable_disabled = models.BooleanField(verbose_name="¿Apto para discapacitado?",default=False)
    description = models.TextField(verbose_name="descripcion")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Destino"
        verbose_name_plural = "Destinos"
        ordering = ['-created']

    def __str__(self):
        return self.name