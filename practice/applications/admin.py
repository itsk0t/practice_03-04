from django.contrib import admin

from applications.models import Application, Status

admin.site.register(Application)
admin.site.register(Status)
