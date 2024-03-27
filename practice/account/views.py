from django.shortcuts import render
from django.contrib.auth.models import User
from applications.models import Application
from vacancies.models import Vacancies


def get_user_id(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return user_id


def account_view(request):
    current_user = request.user
    your_appli = Application.objects.filter(user_id=current_user)
    your_vac = Vacancies.objects.filter(employer_id=current_user)

    return render(request, 'account/account.html', {'your_appli': your_appli,
                                                    'your_vac': your_vac})
