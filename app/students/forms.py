from .models import Student, StudentSubject
from django import forms

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = [
      'room',
            'first_name',
            'last_name',
    ]

class StudentSubjectForm(forms.ModelForm):
	class Meta:
		model = StudentSubject
		fields = [
			'subject',
		]
