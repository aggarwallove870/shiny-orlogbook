from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Graphs)
admin.site.register(Institution)
admin.site.register(Supervisor)