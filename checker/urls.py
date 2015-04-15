from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^track/$', views.track, name='track'),
	url(r'^remove/$', views.remove, name='remove'),
	url(r'^works/$', views.it_works, name='works'),
	url(r'^removeworks/$', views.remove_works, name='remove_works')
]