from django.conf.urls import url
from .views import (
    SubjectView,
    SubjectDeleteView
  )

urlpatterns = [
    url(r'^$', SubjectView.as_view()),
    url(r'^(?P<pk>[0-9]+)/delete/$', SubjectDeleteView.as_view()),
]
