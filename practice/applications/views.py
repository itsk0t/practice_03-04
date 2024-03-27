from django.shortcuts import render
from django.views.generic import DeleteView

from applications.models import Application


class ApplicationDeleteView(DeleteView):
    model = Application
    success_url = '/account/'
    template_name = 'applications/applications_delete.html'
