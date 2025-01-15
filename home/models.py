from django.db import models
import uuid
import os

class Carrusel(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    image = models.ImageField(upload_to="carrusel/img/", null=True, blank=True)
    title = models.CharField(max_length=160, blank=True, null=True)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Verifica si el objeto ya existe antes de intentar acceder a él
        if self.pk and Carrusel.objects.filter(pk=self.pk).exists():
            old_instance = Carrusel.objects.get(pk=self.pk)
            # Si la imagen cambia, borra la anterior del sistema de archivos
            if old_instance.image and self.image != old_instance.image:
                if os.path.isfile(old_instance.image.path):
                    os.remove(old_instance.image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Borra la imagen asociada cuando se elimina el objeto
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)
        
    class Meta:
        db_table = "carrusels"
        verbose_name = "Carrusel"
        verbose_name_plural = "Carrusels"