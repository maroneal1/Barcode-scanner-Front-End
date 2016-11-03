from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

app_name = "questions"

urlpatterns = [
    url(r'^$', views.locations, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^devices/$',views.devices,name='devices'),
    #url(r'^device/view/(?P<dev_pk>[0-9]+)/$',views.deviceView,name="deviceView"),
    url(r'^location/$',views.locations, name='location'),
    url(r'^location/add/$',views.locationsadd, name='locationadd'),
    #url(r'^location/view/(?P<loc_pk>[0-9]+)/$',views.locationView,name="locationView"),
    url(r'^questionsbyuser/$', views.questionsbyuser, name='questionsbyuser'),
    url(r'^addlocation/$', views.addlocation, name='addlocation'),
    url(r'^addanswers$', views.addanswers, name='addanswers'),

    ]
