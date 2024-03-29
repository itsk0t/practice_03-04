from django.urls import path

from account.views import account_view, your_vac_detail_view, StatusUpdateView

app_name = 'account'

urlpatterns = [
    path('', account_view, name='account'),
    path('<int:pk>/', your_vac_detail_view, name='yor_vacancies_detail'),
    path('<int:pk>/update', StatusUpdateView.as_view(), name='status_update'),
]
