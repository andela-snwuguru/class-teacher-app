from django.conf.urls import url
from .views import (
    ClassRoomList,
    ClassRoomCreate,
    ClassRoomDetail,
    ClassRoomUpdate,
    ClassRoomDelete,
  )

urlpatterns = [
    url(r'^$', ClassRoomList.as_view()),
    url(r'^create/$', ClassRoomCreate.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', ClassRoomDetail.as_view(), name='classroom-detail'),
    url(r'^(?P<pk>[0-9]+)/delete/$', ClassRoomDelete.as_view()),
    url(r'^(?P<pk>[0-9]+)/edit/$', ClassRoomUpdate.as_view()),
]
