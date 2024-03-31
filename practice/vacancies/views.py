from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.views.generic.edit import FormMixin

from applications.forms import ApplicationForm
from vacancies.forms import VacanciesCreateForm
from vacancies.models import Vacancies, CategoryVacancies


# class VacanciesListView(ListView):
#     model = Vacancies
#     template_name = 'vacancies/vac_list.html'
#     context_object_name = 'vac'
#     ordering = '-date'

def vacancies_list_view(request):
    categories = CategoryVacancies.objects.all()
    vacancies = Vacancies.objects.all()

    if request.method == 'GET':
        min_price = request.GET.get('min_price')

        if min_price:
            vacancies = vacancies.filter(salary__gte=min_price)

    if request.method == 'GET':
        selected_categories = request.GET.getlist('category')
        if selected_categories:
            vacancies = vacancies.filter(category_id__title__in=selected_categories)

    return render(request, 'vacancies/vac_list.html', {'categories': categories, 'vacancies': vacancies})


class VacanciesDetailView(FormMixin, DetailView):
    model = Vacancies
    template_name = 'vacancies/vac_detail.html'
    context_object_name = 'vac_detail'
    form_class = ApplicationForm
    success_url = '/account/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.vacancies_id = self.get_object()
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


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
