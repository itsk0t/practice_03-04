from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from auth.views import RegisterUserView, LoginUserView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('auth:login')), name='logout')
]