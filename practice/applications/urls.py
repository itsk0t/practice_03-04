from django.urls import path

from applications.views import ApplicationDeleteView

app_name = 'account'

urlpatterns = [
    path('<int:pk>/delete', ApplicationDeleteView.as_view(), name='appli_delete'),
]
