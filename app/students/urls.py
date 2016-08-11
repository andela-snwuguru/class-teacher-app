from django.conf.urls import url
from .views import (
    StudentList,
    StudentCreate,
    StudentDetail,
    StudentUpdate,
    StudentDelete,
  )

urlpatterns = [
    url(r'^$', StudentList.as_view()),
    url(r'^create/$', StudentCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetail.as_view(), name='student-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', StudentDelete.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit/$', StudentUpdate.as_view()),
]
