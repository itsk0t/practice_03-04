from django import forms

from vacancies.models import Vacancies


class VacanciesCreateForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = ['image',
                  'title',
                  'salary',
                  'category_id',
                  'schedule',
                  'payments',
                  'experience',
                  'including_for',
                  'inventory',
                  'address',
                  'description'
                  # 'date'
                  ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Название'}),
            'salary': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Зарпалата'}),
            'category_id': forms.Select(),
            'schedule': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'График работы'}),
            'payments': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Частота выплат'}),
            'experience': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Опыт работы'}),
            'including_for': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'В том числе для кандидатов'}),
            'inventory': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Что получают работники'}),
            'address': forms.TextInput(attrs={'class': 'form-control w-75', 'placeholder': 'Адрес'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-75', 'placeholder': 'Описание'}),
            # 'date': forms.DateTimeField(attrs={'class': 'form-control w-75', 'placeholder': 'Дата публикации'}),
            # 'image': forms.ImageField(),
            'employer_id': forms.IntegerField()
        }