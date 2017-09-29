from django.conf.urls import url

from podcasteryapp import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^second/$', views.second, name='second')
]