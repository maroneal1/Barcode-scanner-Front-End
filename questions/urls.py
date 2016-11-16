from django.conf.urls import url

from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

app_name = "questions"

urlpatterns = [
    url(r'^$', views.locations, name='index'),
    #url(r'^add/$', views.add, name='add'),
    url(r'^devices/$',views.devices,name='devices'),
    url(r'^device/view/(?P<dev_pk>[0-9]+)/$',views.deviceView.as_view(),name="deviceView"),
    url(r'^location/$',views.locations, name='location'),
    url(r'^location/add/$',views.locationsadd, name='locationadd'),
    url(r'^device/add/$',views.deviceadd, name='deviceadd'),
    url(r'^location/view/(?P<loc_pk>[0-9]+)/$',views.locationView,name="locationView"),
    url(r'^questionsbyuser/$', views.questionsbyuser, name='questionsbyuser'),
    url(r'^addlocation/$', views.addlocation, name='addlocation'),
    url(r'^adddevice/$', views.adddevice, name='adddevice'),
    url(r'^addanswers/$', views.addanswers, name='addanswers'),
    url(r'^users$', views.users, name='users'),
    url(r'^login/$', auth_views.login),

    ]
