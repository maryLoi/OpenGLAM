from django.contrib import admin

from . import models

admin.site.register(models.ProjectComment)
admin.site.register(models.Project)