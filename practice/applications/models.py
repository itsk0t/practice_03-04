from django.contrib.auth.models import User
from django.db import models

from vacancies.models import Vacancies


class Status(models.Model):
    title = models.CharField('Статус', max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Application(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    vacancies_id = models.ForeignKey(Vacancies, on_delete=models.CASCADE, verbose_name='Вакансия')
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, default=1, verbose_name='Статус заявки')
    full_name = models.CharField('ФИО', max_length=256)
    phone_number = models.CharField('Номер телефона', max_length=32)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
