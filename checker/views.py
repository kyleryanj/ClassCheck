import sys
sys.path.insert(0, '/home/kyleryanj/Downloads/Programming/ClassCheck/ClassCheck/ClassCheck/')

from dev_settings import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from .forms import StudentForm

from twilio.rest import TwilioRestClient 

from .models import Class, Student

def index(request):
	return render(request, 'checker/index.html')

def track(request):
	# name_form = NameForm()
	# class_form = ClassForm()
	# email_form = EmailForm()
	# number_form = NumberForm()
	# forms = {
	# 	'class_form': class_form,
	# 	'email_form': email_form,
	# 	'number_form': number_form,
	# 	'name_form': name_form,
	# }
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			name = form.cleaned_data['name'].lower()
			email = form.cleaned_data['email'].lower()
			number = form.cleaned_data['phone_number'].lower()

			# if email != '' and number != '':
			# 	raise ValidationError(('You cannot enter both an email and a phone number'))

			classes=[]
			class_code = form.cleaned_data['class_code'].lower()
			class_code2 = form.cleaned_data['class_code2'].lower()
			class_code3 = form.cleaned_data['class_code3'].lower()
			classes.append(class_code)
			classes.append(class_code2)
			classes.append(class_code3)

			#get rid of duplicates
			classes = list(set(classes))

			#add classes to list and remove non-entries
			for item in classes:
				if item == "":
					classes.remove(item)


			if len(Student.objects.filter(phone_number=number)) != 0 or len(Student.objects.filter(email=email)) != 0:
				return render(request, 'checker/track.html', {'form': form, 'error_message': "That student already exists.",})

			#here is awful hard-coding into db	
			if number == '':
				new_student = Student(name=name, email=email, phone_number="none")
			else:
				new_student = Student(name=name, email="none", phone_number=number)

			new_student.save()

			for class_code_item in classes:
				if len(Class.objects.filter(class_code=class_code_item)) != 0:
					existing_class = Class.objects.get(class_code=class_code_item)
					existing_class.students.add(new_student)
				else:
					new_class = Class(class_code=class_code_item)
					new_class.save()
					new_class.students.add(new_student)

			if number != '':
				ACCOUNT_SID = "***REMOVED***"
				AUTH_TOKEN = "***REMOVED***"
				client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
	
				client.messages.create(to=number, from_="***REMOVED***", body="Thanks for using ClassCheck! This message is to confirm that your contact information is correct.")
			else:
				send_mail('ClassCheck Confirmation', 'Thanks for using ClassCheck! This message is to confirm that your contact information is correct.', 'ryanwn@bc.edu', [email], fail_silently=False)

			return HttpResponseRedirect(reverse('works'))
	else:
		form = StudentForm()
	return render(request, 'checker/track.html', {'form': form, })

def remove(request):
	return HttpResponse("remove page")

def track_submit(request, forms):
	name = request.POST['name']
	email = request.POST['email']
	class_code = request.POST['class']
	number = request.POST['number']

	if name in Student.objects.all().name or email in Student.objects.all().email:
		return render(request, 'checker/track.html', forms.update({'error_message': "That student already exists"}))
	new_student = Student(name=name, email=email, number=number)
	new_student.save()

	if class_code in Class.objects.all().class_code:
		existing_class = Class.objects.get(class_code=class_code)
		existing_class.students.add(new_student)
	else:
		new_class = Class(class_code=class_code)
		new_class.save()
		new_class.students.add(new_student)


	return HttpResponseRedirect(reverse('works'))

def remove_submit(request):
	return HttpResponse("removesubmit page")

def it_works(request):
	return HttpResponse("Yesssss")