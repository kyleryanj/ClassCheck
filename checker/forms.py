from django import forms

class NameForm(forms.Form):
	name = forms.CharField(label="Name", max_length=25, required=False)

class NumberForm(forms.Form):
	phone_number = forms.RegexField(required=False, label="Number", regex=r'^\+1\d{10}$', error_message= ("Phone number must be entered in the format: '+19999999999'."))

class EmailForm(forms.Form):
	email = forms.EmailField(label="Email", max_length=70, required=False)

class ClassForm(forms.Form):
	class_code = forms.RegexField(label="Class", regex=r'^[A-Fa-f]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101"))

