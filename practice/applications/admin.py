from django.contrib import admin

from applications.models import Application, Status, Comments

admin.site.register(Application)
admin.site.register(Status)
admin.site.register(Comments)
