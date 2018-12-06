from django.contrib import admin
from .models import Question

# Register your models here.
admin.site.register(Question) # Indique à l'admin que l'objet Question a une interface d'administration
