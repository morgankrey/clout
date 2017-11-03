from django.conf.urls import url

from podcasteryapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^read/(?P<read_id>\d+)/$', views.read_detail, name='read_detail'),
	url(r'^read/new$', views.read_new, name='read_new'),
	url(r'^read/(?P<read_id>\d+)/edit/$', views.read_edit, name='read_edit'),
	url(r'^slot/(?P<slot_id>\d+)/$', views.slot_detail, name='slot_detail'),
	url(r'^slot/new$', views.slot_new, name='slot_new'),
	url(r'^slot/(?P<slot_id>\d+)/edit/$', views.slot_edit, name='slot_edit'),
]