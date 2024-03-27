from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from vacancies.forms import VacanciesCreateForm
from vacancies.models import Vacancies


class VacanciesListView(ListView):
    model = Vacancies
    template_name = 'vacancies/vac_list.html'
    context_object_name = 'vac'


class VacanciesDetailView(DetailView):
    model = Vacancies
    template_name = 'vacancies/vac_detail.html'
    context_object_name = 'vac_detail'


def vacancies_create_view(request):
    form = VacanciesCreateForm(request.POST, request.FILES)
    if form.is_valid():
        vacancies = form.save(commit=False)
        vacancies.employer_id = request.user
        vacancies.save()

        return redirect('vacancies:vac_list')

    else:
        form = VacanciesCreateForm()

    return render(request, 'vacancies/vac_create.html', {'form': form})
