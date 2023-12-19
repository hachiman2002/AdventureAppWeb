from django.db import models

# Create your models here.
class Events(models.Model):
    id_event = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Nombre Evento", max_length=50)
    date_event = models.DateTimeField(verbose_name="Fecha Evento")
    description = models.TextField(verbose_name="Descripción")
    mainImage = models.ImageField(verbose_name="Imagen Portada", upload_to='events',blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['-created']

    def __str__(self):
        return self.name
