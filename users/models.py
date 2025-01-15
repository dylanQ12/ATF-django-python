from django.db import models
from django.contrib.auth.models import AbstractUser
import os


class CustomUser(AbstractUser):
    photo = models.ImageField(
        upload_to="usuarios/fotos/",
        blank=True,
        null=True,
        verbose_name="Foto de perfil",
    )

    first_name = models.CharField(max_length=150, verbose_name="Nombres")
    last_name = models.CharField(max_length=150, verbose_name="Apellidos")
    username = models.CharField(
        max_length=150, unique=True, verbose_name="Nombre de usuario"
    )
    email = models.EmailField(verbose_name="Correo electrónico")
    is_staff = models.BooleanField(
        default=False,
        help_text="Indica si este usuario puede iniciar sesión en el sitio de administración.",
        verbose_name="Es personal",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indica si este usuario debe ser tratado como activo. Desmarque esto en lugar de eliminar cuentas.",
        verbose_name="Está activo",
    )
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de registro"
    )
    last_login = models.DateTimeField(
        null=True, blank=True, verbose_name="Último inicio de sesión"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = CustomUser.objects.get(pk=self.pk)
            if old_instance.photo and self.photo != old_instance.photo:
                if os.path.isfile(old_instance.photo.path):
                    os.remove(old_instance.photo.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    # Definir related_name para evitar conflictos
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        help_text="Los grupos a los que pertenece este usuario.",
        verbose_name="Grupos",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",
        blank=True,
        help_text="Permisos específicos para este usuario.",
        verbose_name="Permisos de usuario",
    )

    class Meta:
        db_table = "users"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
