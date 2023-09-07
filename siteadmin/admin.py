from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.news)
admin.site.register(models.socialmedia)
admin.site.register(models.category)
admin.site.register(models.herosection)