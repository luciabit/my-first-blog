from django.db import models
from django.utils import timezone


class Post(models.Model):
	author = models.ForeignKey('auth.User') # link ad un altro modello
	title = models.CharField(max_length=200) #testo con numero limitato di lettere
	text = models.TextField() # testo senza limite
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True) # non obbligatorio, può avere un valore nullo 

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		#return self.title
		return '%s' % (self.title)

