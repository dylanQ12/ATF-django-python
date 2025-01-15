from django.db import models
from users.models import CustomUser
import uuid
import os


class Post(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    image = models.ImageField(upload_to="blog/img/", null=True, blank=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="author_posts",
        verbose_name="Author",
    )

    def save(self, *args, **kwargs):
        # Verifica si el objeto ya existe antes de intentar acceder a él
        if self.pk and Post.objects.filter(pk=self.pk).exists():
            old_instance = Post.objects.get(pk=self.pk)
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
        db_table = "posts"
        verbose_name = "Publicacion"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return f"{self.title} - {self.author}"
