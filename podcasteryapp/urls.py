from django.conf.urls import url

from podcasteryapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^profile/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
    
    url(r'^show/new/$', views.show_new, name='show_new'),
    url(r'^show/(?P<show_id>\d+)/$', views.show_detail, name='show_detail'),
    url(r'^show/(?P<show_id>\d+)/edit/$', views.show_edit, name='show_edit'),

	url(r'^read/(?P<read_id>\d+)/$', views.read_detail, name='read_detail'),
	url(r'^read/new$', views.read_new, name='read_new'),
	url(r'^read/(?P<read_id>\d+)/edit/$', views.read_edit, name='read_edit'),

	url(r'^slot/(?P<slot_id>\d+)/$', views.slot_detail, name='slot_detail'),
	url(r'^slot/new$', views.slot_new, name='slot_new'),
	url(r'^slot/(?P<slot_id>\d+)/edit/$', views.slot_edit, name='slot_edit'),

	url(r'^episode/(?P<episode_id>\d+)/$', views.episode_detail, name='episode_detail'),
]