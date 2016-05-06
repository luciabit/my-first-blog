from django.conf.urls import include, url
from . import views # col . indico la cartella dello stesso livello

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),  # '^$' significa stringa vuota (combina un inizio con una fine)
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]