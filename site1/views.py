from django.shortcuts import render
from django.utils import timezone
from .models import Historia
from .models import Agenda

def post_list(request):
	historia = Historia.objects.first()
	agenda = Agenda.objects.all()
	return render(request, 'site1/post_list.html', 
		{'historia':historia, 
		'agenda':agenda})
		
def main_site(request):
	historia = Historia.objects.first()
	agenda = Agenda.objects.all()
	return render(request, 'site1/index.html', 
		{'historia':historia, 
		'agenda':agenda})