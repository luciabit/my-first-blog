from django.contrib import admin
from .models import Post

admin.site.register(Post) # registro il modello per renderlo visibile su admin
