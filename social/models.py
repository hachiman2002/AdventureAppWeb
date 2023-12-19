from django.db import models


class Social(models.Model):
    name_key = models.SlugField(
        verbose_name="Nombre clave",
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        validators=[], 
    )
    name = models.CharField(verbose_name="Red social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
