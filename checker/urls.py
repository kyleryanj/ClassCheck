from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^track/$', views.track, name='track'),
	url(r'^remove/$', views.remove, name='remove'),
	url(r'^tracksubmit/$', views.track_submit, name='track_submit'),
	url(r'^removesubmit/$', views.remove_submit, name='remove_submit'),
]