from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class CreateNewSchema(forms.Form):
	name = forms.CharField(label="Name", max_length = 50)
	check1 = forms.BooleanField(label="Full name", required=False, initial=True)
	check2 = forms.BooleanField(label="PersonId", required=False, initial=True)
	check3 = forms.BooleanField(label="E-mail", required=False, initial=True)
	check4 = forms.BooleanField(label="Phone number", required=False, initial=True)
	check5 = forms.BooleanField(label="Address", required=False, initial=True)
	check6 = forms.BooleanField(label="Job", required=False, initial=True)
	check7 = forms.BooleanField(label="Company name", required=False, initial=True)
	n = forms.IntegerField(label="Number of fields", validators=[MaxValueValidator(100), MinValueValidator(1)])