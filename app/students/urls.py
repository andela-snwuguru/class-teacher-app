from django.conf.urls import url
from .views import (
    StudentList,
    StudentCreate,
    StudentDetail,
    StudentUpdate,
    StudentDelete,
    StudentSubjectView,
    StudentSubjectDeleteView,
  )

urlpatterns = [
    url(r'^$', StudentList.as_view()),
    url(r'^create/$', StudentCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetail.as_view(), name='student-detail'),
    url(r'^(?P<pk>[0-9]+)/subject/$', StudentSubjectView.as_view()),
    url(r'^(?P<pk>[0-9]+)/subject/(?P<student_subject_id>[0-9]+)/$', StudentSubjectDeleteView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit/$', StudentUpdate.as_view()),
]
