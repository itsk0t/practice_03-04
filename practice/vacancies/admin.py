from django.contrib import admin

from vacancies.models import Vacancies, CategoryVacancies

admin.site.register(Vacancies)
admin.site.register(CategoryVacancies)
