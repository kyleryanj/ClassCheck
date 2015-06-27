from django import forms


class StudentForm(forms.Form):
	name = forms.CharField(label="Name: ", max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Optional', 'class':'form-control'}))
	choice = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), label="Choose Email or Phone Number: ", choices=(('email', 'Email'), ('phone', 'Phone Number')), required=True)
	contact_info = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Email or Phone number in +19999999999 format', 'class':'form-control'}), label="Email/Phone Number: ", regex=r'^(\+1\d{10})|[^@]+@[^@]+\.[^@]+$', error_message= ("Must enter number in +19999999999 format or valid email address"))
	# phone_number = forms.RegexField(required=False, label="Phone Number", regex=r'^\+1\d{10}$', error_message= ("Phone number must be entered in the format: '+19999999999'."))
	# email = forms.EmailField(label="Email", max_length=70, required=False)
	class_code = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': '*Full* valid class code e.g. CSCI110101', 'class':'form-control'}), label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code2 = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code3 = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))


class RemoveForm(forms.Form):
	choice = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), label="Did you register with an email or phone number?", choices=(('email', 'Email'), ('phone', 'Phone Number')), required=True)
	contact_info = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Email or Phone number in +19999999999 format', 'class':'form-control'}), label="Email/number", regex=r'^(\+1\d{10})|[^@]+@[^@]+\.[^@]+$', error_message= ("Must enter number in +19999999999 format or valid email address"))

class AddClassForm(forms.Form):
	choice = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), label="Did you register with an email or phone number?", choices=(('email', 'Email'), ('phone', 'Phone Number')), required=True)
	contact_info = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Email or Phone number in +19999999999 format', 'class':'form-control'}), label="Email/Number: ", regex=r'^(\+1\d{10})|[^@]+@[^@]+\.[^@]+$', error_message= ("Must enter number in +19999999999 format or valid email address"))
	class_code = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': '*Full* valid class code e.g. CSCI110101', 'class':'form-control'}), label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code2 = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))
	class_code3 = forms.RegexField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, label="Class code: ", regex=r'^[A-Za-z]{4}\d{6}$', error_message= ("Invalid course code. Should be code+section e.g. csci110101."))

class ListClassForm(forms.Form):
	choice = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), label="Did you register with an email or phone number?", choices=(('email', 'Email'), ('phone', 'Phone Number')), required=True)
	contact_info = forms.RegexField(widget=forms.TextInput(attrs={'placeholder': 'Email or Phone number in +19999999999 format', 'class':'form-control'}), label="Email/Number: ", regex=r'^(\+1\d{10})|[^@]+@[^@]+\.[^@]+$', error_message= ("Must enter number in +19999999999 format or valid email address"))

