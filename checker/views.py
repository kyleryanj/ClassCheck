from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm, ClassForm, EmailForm, NumberForm

def index(request):
	return render(request, 'checker/index.html')

def track(request):
	name_form = NameForm()
	class_form = ClassForm()
	email_form = EmailForm()
	number_form = NumberForm()
	forms = {
		'class_form': class_form,
		'email_form': email_form,
		'number_form': number_form,
		'name_form': name_form,
	}
	return render(request, 'checker/track.html', forms)

def remove(request):
	return HttpResponse("remove page")

def track_submit(request):
	return HttpResponse("tracksubmit page")

def remove_submit(request):
	return HttpResponse("removesubmit page")