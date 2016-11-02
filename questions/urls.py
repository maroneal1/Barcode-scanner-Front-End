from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.devices, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^devices/$',views.devices,name='devices'),
    url(r'^location/$',views.locations, name='location'),
    url(r'^location/add/$',views.locationsadd, name='locationadd'),
    url(r'^questionsbyuser/$', views.questionsbyuser, name='questionsbyuser'),
    url(r'^addlocation/$', views.addlocation, name='addlocation'),

    ]
