from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Alpha$', views.Alpha, name='Alpha'),
    url(r'^timeleft$', views.index, name='index'),

]
