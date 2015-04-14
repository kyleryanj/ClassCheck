from django import forms


class StudentForm(forms.Form):
	name = forms.CharField(label="Name", max_length=25, required=False)
	phone_number = forms.RegexField(required=False, label="Phone Number", regex=r'^\+1\d{10}$', error_message= ("Phone number must be entered in the format: '+19999999999'."))
	email = forms.EmailField(label="Email", max_length=70, required=False)
	class_code = forms.RegexField(label="Class code", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code2 = forms.RegexField(required=False, label="Class code", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code3 = forms.RegexField(required=False, label="Class code", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))

	# def clean(self):
	# 	if not(self.phone_number or self.email):
	# 		raise ValidationError("You must enter either a phone number or email.")

	# 	if self.phone_number != '' and self.email != '':
	# 		raise ValidationError("You cannot enter both an email and phone number.")

class RemoveForm(forms.Form):
	choice = forms.ChoiceField(label="Did you register with an email or phone number?", choices=(('email', 'Email'), ('phone', 'Phone Number')), required=True)
	contact_info = forms.RegexField(label="Email/number", regex=r'^(\+1\d{10})|[^@]+@[^@]+\.[^@]+$', error_message= ("Must enter number in +19999999999 format or valid email address"))
# class NameForm(forms.Form):

# class NumberForm(forms.Form):
# 	phone_number = forms.RegexField(required=False, label="Number", regex=r'^\+1\d{10}$', error_message= ("Phone number must be entered in the format: '+19999999999'."))

# class EmailForm(forms.Form):
# 	email = forms.EmailField(label="Email", max_length=70, required=False)

# class ClassForm(forms.Form):
# 	class_code = forms.RegexField(label="Class", regex=r'^[A-Fa-f]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101"))

