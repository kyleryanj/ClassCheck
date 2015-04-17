from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^track/$', views.track, name='track'),
	url(r'^remove/$', views.remove, name='remove'),
	url(r'^add/$', views.add_class, name='add_class'),
	url(r'^list/$', views.list_class_form, name='list_class_form'),
	url(r'^faq/$', views.faq, name='faq'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^privacy/$', views.privacy, name='privacy'),
]