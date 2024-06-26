from django.urls import path

from vacancies.views import VacanciesDetailView, vacancies_create_view, VacanciesDeleteView, \
    VacanciesUpdateView, Search, vacancies_list_view

app_name = 'vacancies'

urlpatterns = [
    path('vacancies_list/', vacancies_list_view, name='vac_list'),
    path('<int:pk>/', VacanciesDetailView.as_view(), name='vac_detail'),
    path('vacancies_create', vacancies_create_view, name='vac_create'),
    path('<int:pk>/delete', VacanciesDeleteView.as_view(), name='vac_delete'),
    path('<int:pk>/update', VacanciesUpdateView.as_view(), name='vac_update'),
    path('search/', Search.as_view(), name='search'),
]
