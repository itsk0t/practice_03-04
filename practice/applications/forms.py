from django import forms
from applications.models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['vacancies_id',
                  'full_name',
                  'phone_number',
                  ]

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'ФИО'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Номер телефона'}),
            'vacancies_id': forms.IntegerField(),
            'user_id': forms.IntegerField()
        }