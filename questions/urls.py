from django.conf.urls import url

from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^questionsbyuser$', views.questionsbyuser, name='questionsbyuser'),
    url(r'^addlocation$', views.addlocation, name='addlocation'),

    ]
