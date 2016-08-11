from django.test import TestCase
from students.models import Student, StudentSubject
from subject.models import Subject
# Create your tests here.

class StudentSubjectTest(TestCase):

    def setUp(self):
      self.student = Student.objects.create(first_name='sun', last_name='nwu')
      self.subject = Subject.objects.create(title='math')

    def test_student_assign_subject(self):
        response = self.assign_subject()
        self.assertEqual(response.status_code, 302)
        
    def assign_subject(self):
        return self.client.post(
          '/students/' + str(self.student.id) + '/subject/', 
          {'student': self.student.id, 'subject': self.subject.id}
        )

    def test_student_list_subject(self):
        self.assign_subject()
        response = self.client.get('/students/' + str(self.student.id) + '/subject/')
        self.assertEqual(response.status_code, 200)
        
    def test_subject_delete(self):
        self.assign_subject()
        assigned = StudentSubject.objects.get()
        response = self.client.get('/students/' + str(self.student.id) + '/subject/' + str(assigned.id) + '/')
        self.assertEqual(response.status_code, 302)
        