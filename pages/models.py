from django.db import models


class Pages(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = models.TextField(verbose_name="Contenido", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
