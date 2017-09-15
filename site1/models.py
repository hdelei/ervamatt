from django.db import models
from django.utils import timezone

class Historia(models.Model):
    #author = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200,
            verbose_name="Título do cabeçalho")
    texto = models.TextField(verbose_name="Hitória da banda")


    def __str__(self):
        return self.titulo


    class Meta:
        verbose_name = 'História'
        verbose_name_plural = 'História'


class Agenda(models.Model):
    #author = models.ForeignKey('auth.User')
    local = models.CharField(max_length=200,
            verbose_name='Local do Evento')
    endereco = models.CharField(max_length=200,
            verbose_name='Endereço')
    data = models.DateTimeField(default=timezone.now,
            verbose_name='Data do evento')
    img = models.ImageField(upload_to = 'ervamatt/static/img_schedule',
			default = 'ervamatt/static/img_schedule/sched.png',
			blank=True,
			verbose_name="Foto ou logotipo do local")


    def get_name(self):
        img_name = self.img.url.replace('ervamatt/', '')
        return img_name


    def __str__(self):
        return self.local


    class Meta:
        verbose_name = 'Agenda de shows'
        verbose_name_plural = 'Agenda de shows'
