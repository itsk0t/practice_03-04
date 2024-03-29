from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.views.generic import DetailView, UpdateView

from applications.forms import CommentsForm
from applications.models import Application, Comments
from vacancies.models import Vacancies


def get_user_id(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return user_id


def account_view(request):
    current_user = request.user
    your_appli = Application.objects.filter(user_id=current_user)
    comments_appli = Comments.objects.all()  # Надо доделать
    your_vac = Vacancies.objects.filter(employer_id=current_user)

    return render(request, 'account/account.html', {'your_appli': your_appli,
                                                    'your_vac': your_vac,
                                                    'comments_appli': comments_appli})


def your_vac_detail_view(request, pk):
    y_vac_det = get_object_or_404(Vacancies, pk=pk)
    appli_vac_detail = Application.objects.filter(vacancies_id=pk)

    form = CommentsForm(request.POST, request.FILES)
    if form.is_valid():
        vacancies = form.save(commit=False)
        vacancies.user_id = request.user
        vacancies.save()

    else:
        form = CommentsForm()

    return render(request, 'account/your_vac_detail.html',
                  {'y_vac_det': y_vac_det, 'appli_vac_detail': appli_vac_detail, 'form': form})

