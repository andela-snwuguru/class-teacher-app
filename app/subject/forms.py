from .models import Subject
from django import forms

class SubjectForm(forms.ModelForm):
	class Meta:
		model = Subject
		fields = [
			'title',
		]
