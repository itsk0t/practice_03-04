from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from applications.models import Application
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


class VacanciesDeleteView(DeleteView):
    model = Vacancies
    success_url = '/account/'
    template_name = 'vacancies/vac_delete.html'


class VacanciesUpdateView(UpdateView):
    model = Vacancies
    template_name = 'vacancies/vac_create.html'
    success_url = '/account/'
    form_class = VacanciesCreateForm


class Search(ListView):

    template_name = 'vacancies/vac_list.html'
    context_object_name = 'vac'

    def get_queryset(self):
        return Vacancies.objects.filter(title__iregex=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
