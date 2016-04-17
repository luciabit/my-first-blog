from django.conf.urls import url
from . import views # col . indico la cartella dello stesso livello

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),  # '^$' significa stringa vuota (combina un inizio con una fine)
]