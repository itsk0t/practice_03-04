from django.urls import path

from applications.views import ApplicationDeleteView, application_view

app_name = 'applications'

urlpatterns = [
    path('', application_view, name='appli'),
    path('<int:pk>/delete', ApplicationDeleteView.as_view(), name='appli_delete'),
]
