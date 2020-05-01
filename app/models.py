from django.db import models

# Create your models here.
class Perfil(models.Model):
	titulo = models.CharField(max_length=200, null=True)
	foto = models.ImageField(default="profile1.png", null=True, blank=True)


    def __str__(self):
        return self.titulo