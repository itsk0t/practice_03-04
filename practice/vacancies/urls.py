from django.urls import path

from vacancies.views import VacanciesListView, VacanciesDetailView, vacancies_create_view

app_name = 'vacancies'

urlpatterns = [
    path('vacancies_list/', VacanciesListView.as_view(), name='vac_list'),
    path('<int:pk>/', VacanciesDetailView.as_view(), name='vac_detail'),
    path('vacancies_create', vacancies_create_view, name='vac_create')
]
