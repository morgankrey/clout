from django.conf.urls import url

from podcasteryapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^reads/(?P<read_id>\d+)/', views.read_detail, name='read detail'),
	url(r'^slots/(?P<slot_id>\d+)/', views.slot_detail, name='slot detail')
]