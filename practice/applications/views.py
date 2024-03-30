from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from applications.forms import ApplicationForm
from applications.models import Application, Vacancies


class ApplicationDeleteView(DeleteView):
    model = Application
    success_url = '/account/'
    template_name = 'applications/applications_delete.html'
