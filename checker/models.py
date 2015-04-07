from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
	phone_regex = RegexValidator(regex=r'^\+1\d{10}$', message="Phone number must be entered in the format: '+19999999999'.")
	phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=12)
	email = models.EmailField(max_length=70, blank=True)

class Class(models.Model):
	class_regex = RegexValidator(regex=r'^[A-Fa-f]{4}\d{6}', message="Invalid course code. Should be code+section e.g. csci110101")
	class_code = models.CharField(validators=[class_regex], blank=True, max_length=10)
	students = models.ManyToManyField(Student)

