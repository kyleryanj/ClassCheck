from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^track/$', views.track, name='track'),
	url(r'^remove/$', views.remove, name='remove'),
	url(r'^works/$', views.it_works, name='works'),
	url(r'^removeworks/$', views.remove_works, name='remove_works'),
	url(r'^add/$', views.add_class, name='add_class'),
	url(r'^addworks/$', views.add_class_works, name='add_class_works'),
	url(r'^list/$', views.list_class_form, name='list_class_form'),
	url(r'^test/$', views.test, name='test'),
]