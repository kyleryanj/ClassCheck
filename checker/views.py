from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import StudentForm

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
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			class_code = form.cleaned_data['class_code']
			number = form.cleaned_data['phone_number']

			if len(Student.objects.filter(phone_number=number)) != 0 or len(Student.objects.filter(email=email)) != 0:
				return render(request, 'checker/track.html', {'form': form, 'error_message': "That student already exists.",})

			new_student = Student(name=name, email=email, phone_number=number)
			new_student.save()

			if class_code in Class.objects.all().values().values():
				existing_class = Class.objects.get(class_code=class_code)
				existing_class.students.add(new_student)
			else:
				new_class = Class(class_code=class_code)
				new_class.save()
				new_class.students.add(new_student)


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