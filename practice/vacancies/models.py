from django.contrib.auth.models import User
from django.db import models


class Vacancies(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')
    title = models.CharField('Название', max_length=64)
    salary = models.CharField('З/п', max_length=64)
    employer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    field_activity = models.CharField('Сфера деятельности', max_length=64)
    schedule = models.CharField('График работы', max_length=64)
    payments = models.CharField('Частота выплат', max_length=64)
    experience = models.CharField('Опыт работы', max_length=64)
    including_for = models.CharField('В том числе для кандидатов', max_length=256)
    inventory = models.CharField('Что получают работники', max_length=256)
    address = models.CharField('Адрес', max_length=256)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
