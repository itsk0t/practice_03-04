from django.shortcuts import render
from django.views.generic import ListView
from vacancies.models import Vacancies


class MainView(ListView):
    queryset = Vacancies.objects.order_by('-date')
    template_name = 'main/main.html'
    context_object_name = 'main'
    paginate_by = 3

