import sys
sys.path.insert(0, '/app/ClassCheck/')

from dev_settings import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.core.exceptions import ValidationError

from .forms import StudentForm, RemoveForm, AddClassForm, ListClassForm

from twilio.rest import TwilioRestClient 

from .models import Class, Student

def index(request):
	return render(request, 'checker/index.html')

def track(request):
	if request.method == 'POST' and 'submit' in request.POST:
		form = StudentForm(request.POST)
		if form.is_valid():
			contact_info = form.cleaned_data['contact_info'].lower()
			choice = form.cleaned_data['choice'].lower()

			name = form.cleaned_data['name'].lower()
			# email = form.cleaned_data['email'].lower()
			# number = form.cleaned_data['phone_number'].lower()

			# if email != '' and number != '':
			# 	raise ValidationError(('You cannot enter both an email and a phone number'))


			if len(Student.objects.filter(phone_number=contact_info)) != 0 or len(Student.objects.filter(email=contact_info)) != 0:
				return render(request, 'checker/track.html', {'form': form, 'error_message': "That student already exists.",})

			#here is awful hard-coding into db	
			#and bad form checking
			if choice == 'email':
				if not contact_info[0] == "+":
					new_student = Student(name=name, email=contact_info, phone_number="none")
				else:
					return render(request, 'checker/track.html', {'form': form, 'error_message': "You selected Email but gave us a phone number!",})
			elif choice == 'phone':
				if '@' not in contact_info:
					new_student = Student(name=name, email="none", phone_number=contact_info)
				else:
					return render(request, 'checker/track.html', {'form': form, 'error_message': "You selected Phone Number but gave us an email!",})

			new_student.save()

			classes=[]
			class_code = form.cleaned_data['class_code'].lower()
			class_code2 = form.cleaned_data['class_code2'].lower()
			class_code3 = form.cleaned_data['class_code3'].lower()
			classes.append(class_code)
			classes.append(class_code2)
			classes.append(class_code3)

			classes = fix_classes(classes)
			

			for class_code_item in classes:
				if len(Class.objects.filter(class_code=class_code_item)) != 0:
					existing_class = Class.objects.get(class_code=class_code_item)
					existing_class.students.add(new_student)
				else:
					new_class = Class(class_code=class_code_item)
					new_class.save()
					new_class.students.add(new_student)

			if choice == 'phone':

				client = TwilioRestClient(twilio_account_sid, twilio_auth_token) 
				client.messages.create(to=contact_info, from_="***REMOVED***", body="Thanks for using ClassCheck! This message is to confirm that we have received your request.")
			
			else:
				send_mail('ClassCheck Confirmation', 'Thanks for using ClassCheck! This message is to confirm that we have receieved your request.', 'ryanwn@bc.edu', [contact_info], fail_silently=False)

			return render(request, 'checker/track_success.html')
	else:
		form = StudentForm()
	return render(request, 'checker/track.html', {'form': form, })

def remove(request):
	if request.method == 'POST' and 'submit' in request.POST:
		form = RemoveForm(request.POST)
		if form.is_valid():
			contact_info = form.cleaned_data['contact_info'].lower()
			choice = form.cleaned_data['choice'].lower()

			if choice == 'email':
				if not contact_info[0] == "+":
					to_remove = Student.objects.filter(email=contact_info)
				else:
					return render(request, 'checker/remove.html', {'form': form, 'error_message': "You selected Email but gave us a phone number!",})
						
			elif choice == 'phone':
				if '@' not in contact_info:
					to_remove = Student.objects.filter(phone_number=contact_info)
				else:
					return render(request, 'checker/remove.html', {'form': form, 'error_message': "You selected Phone Number but gave us an email!",})


			if len(to_remove) != 0:
				classes = list(to_remove[0].class_set.all())
				to_remove.delete()
				for item in classes:
					if len(item.students.all()) == 0:
						item.delete()
			else:
				return render(request, 'checker/remove.html', {'form': form, 'error_message': "That student doesn't exist.",})

			return render(request, 'checker/remove_success.html')
	else:
		form = RemoveForm()
	return render(request, 'checker/remove.html', {'form': form, })



def add_class(request):
	if request.method == 'POST' and 'submit' in request.POST:
		form = AddClassForm(request.POST)
		if form.is_valid():
			contact_info = form.cleaned_data['contact_info'].lower()
			choice = form.cleaned_data['choice'].lower()

			if choice == 'email':
				if not contact_info[0] == "+":
					student = Student.objects.filter(email=contact_info)
				else:
					return render(request, 'checker/add_class.html', {'form': form, 'error_message': "You selected Email but gave us a phone number!",})
						
			elif choice == 'phone':
				if '@' not in contact_info:
					student = Student.objects.filter(phone_number=contact_info)
				else:
					return render(request, 'checker/add_class.html', {'form': form, 'error_message': "You selected Phone Number but gave us an email!",})


			if len(student) != 0:
				classes=[]
				class_code = form.cleaned_data['class_code'].lower()
				class_code2 = form.cleaned_data['class_code2'].lower()
				class_code3 = form.cleaned_data['class_code3'].lower()
				classes.append(class_code)
				classes.append(class_code2)
				classes.append(class_code3)

				classes = fix_classes(classes)

				if (len(classes) + len(student[0].class_set.all())) > 3:
					return render(request, 'checker/add_class.html', {'form': form, 'error_message': "Too many classes! You can only track 3 at a time.",})
				else:
					for class_code_item in classes:
						if len(Class.objects.filter(class_code=class_code_item)) != 0:
							existing_class = Class.objects.get(class_code=class_code_item)
							existing_class.students.add(student[0])
						else:
							new_class = Class(class_code=class_code_item)
							new_class.save()
							new_class.students.add(student[0])

			else:
				return render(request, 'checker/add_class.html', {'form': form, 'error_message': "That student doesn't exist.",})

			return render(request, 'checker/add_class_success.html')
	else:
		form = AddClassForm()
	return render(request, 'checker/add_class.html', {'form': form, })

def list_class_form(request):
	if request.method == 'POST' and 'submit' in request.POST:
		form = ListClassForm(request.POST)
		if form.is_valid():
			contact_info = form.cleaned_data['contact_info'].lower()
			choice = form.cleaned_data['choice'].lower()

			if choice == 'email':
				if not contact_info[0] == "+":
					to_list = Student.objects.filter(email=contact_info)
				else:
					return render(request, 'checker/list_class_form.html', {'form': form, 'error_message': "You selected Email but gave us a phone number!",})
						
			elif choice == 'phone':
				if '@' not in contact_info:
					to_list = Student.objects.filter(phone_number=contact_info)
				else:
					return render(request, 'checker/list_class_form.html', {'form': form, 'error_message': "You selected Phone Number but gave us an email!",})


			if len(to_list) != 0:
				classes = [item.class_code for item in to_list[0].class_set.all()]
			else:
				return render(request, 'checker/list_class_form.html', {'form': form, 'error_message': "That student doesn't exist.",})

			return render(request, 'checker/list_class.html', {'classes': classes,})
	else:
		form = ListClassForm()
	return render(request, 'checker/list_class_form.html', {'form': form, })

def faq(request):
	return render(request, 'checker/faq.html')

def contact(request):
	return render(request, 'checker/contact.html')

def privacy(request):
	return render(request, 'checker/privacy.html')

def fix_classes(classes):
	#get rid of duplicates
	class_list = list(set(classes))

	#add classes to list and remove non-entries
	for item in class_list:
		if item == "":
			class_list.remove(item)
	return class_list

