from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from applications.forms import ApplicationForm
from applications.models import Application


def application_view(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            applications = form.save(commit=False)
            applications.user_id = request.user
            applications.save()

            # return redirect('account:account')
    else:
        form = ApplicationForm()

    return render(request, 'applications/applications.html', {'form': form})


class ApplicationDeleteView(DeleteView):
    model = Application
    success_url = '/account/'
    template_name = 'applications/applications_delete.html'
