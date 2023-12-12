import os
from django.db import models

class Errors(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    module = models.CharField(max_length=100)
    message = models.TextField()
    traceback = models.TextField()

    def __str__(self):
        return f"Error en {self.module} el {self.timestamp}"

class Provinces(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")

    class Meta:
        verbose_name = "provincia"
        verbose_name_plural = "provincias"

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Emails(models.Model):
    address = models.CharField(max_length=200, verbose_name="direccion de correo")
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE, verbose_name="provincia")
    created_at = models.DateTimeField(verbose_name="fecha de creación")
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "correo"
        verbose_name_plural = "correos electrónicos"

    def __str__(self):
        return self.address

class Images(models.Model):
    image = models.ImageField(upload_to='images/', verbose_name='imagen a procesar')
    process = models.BooleanField(default=False, verbose_name='procesada')
    province = models.ForeignKey(Provinces, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Imágen'
        verbose_name_plural = 'Imágenes'

    def save(self, *args, **kwargs):
        if self.pk:
            old_image = Images.objects.get(pk=self.pk).image
            if self.image and self.image != old_image:
                if os.path.isfile(old_image.path):
                    os.remove(old_image.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'Imagen de procesamiento con ID #{self.id}'