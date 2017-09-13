from django.db import models
from django.utils import timezone

class Historia(models.Model):
    #author = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    
    def __str__(self):
        return self.titulo
		
class Agenda(models.Model):
    #author = models.ForeignKey('auth.User')
    local = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    data = models.DateTimeField(
            default=timezone.now)
    img = models.ImageField(upload_to = "site1/static/img_schedule",
			default = '/static/img_schedule/sched.png',
			blank=True)
	#img_name = models.CharField(img.url.replace)

    def __str__(self):
        return self.local
	
	#def is_active(self):
		

'''
class Schedule(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    show_date = models.DateTimeField(
            default=timezone.now)
    img = models.ImageField(upload_to = "static/img_schedule",blank=True)

    def __str__(self):
        return self.title
'''