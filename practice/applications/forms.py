from django import forms
from applications.models import Application, Comments


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
                  'full_name',
                  'phone_number',
                  ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'ФИО'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Номер телефона'}),
            'vacancies_id': forms.Select(),
            'user_id': forms.IntegerField()
        }


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
                  'body',
                  # 'date'
                  ]

        widgets = {
            'user_id': forms.IntegerField(),
            'application_id': forms.Select(),
            'body': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Введите текст'}),
            # 'date': forms.DateTimeField(attrs={'class': 'form-control w-75', 'placeholder': 'Дата публикации'})
        }


class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status_id']

        widgets = {
            'status_id': forms.Select()
        }