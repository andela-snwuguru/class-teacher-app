from .models import ClassRoom
from django import forms

class ClassesForm(forms.ModelForm):
	class Meta:
		model = ClassRoom
		fields = [
			'name',
			'capacity',
		]
