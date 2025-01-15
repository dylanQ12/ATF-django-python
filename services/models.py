from django.db import models
import uuid
import os


class Service(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    image = models.ImageField(upload_to="services/img/", null=True, blank=True)
    name = models.CharField(max_length=160, blank=True, null=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Verifica si el objeto ya existe antes de intentar acceder a él
        if self.pk and Service.objects.filter(pk=self.pk).exists():
            old_instance = Service.objects.get(pk=self.pk)
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
        db_table = "services"
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"

    def __str__(self):
        return f"{self.name} - {self.price}"
