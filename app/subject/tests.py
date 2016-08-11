from django.test import TestCase
from .models import Subject

class SubjectTest(TestCase):

    def test_subject_list(self):
        response = self.client.get('/subjects/')
        self.assertEqual(response.status_code, 200)
        
    def create_subject(self):
        return self.client.post('/subjects/', {'title':'maths'})
        
    def test_subject_create(self):
        response = self.create_subject()
        self.assertEqual(response.status_code, 302)

    def test_subject_delete(self):
        self.create_subject()
        subject = Subject.objects.get()
        response = self.client.get('/subjects/' + str(subject.id) + '/delete/')
        self.assertEqual(response.status_code, 302)