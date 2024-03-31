from django.contrib.auth.models import User
from django.db import models


class CategoryVacancies(models.Model):
    title = models.CharField('Навзвание', max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория вакансий'
        verbose_name_plural = 'Категории вакансий'


class Vacancies(models.Model):
    image = models.ImageField('Изображение', upload_to='images/')
    title = models.CharField('Название', max_length=64)
    salary = models.IntegerField(verbose_name='З/п')
    employer_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    category_id = models.ForeignKey(CategoryVacancies, on_delete=models.CASCADE, verbose_name='Категория', default=1)
    schedule = models.CharField('График работы', max_length=64)
    payments = models.CharField('Частота выплат', max_length=64)
    experience = models.CharField('Опыт работы', max_length=64)
    including_for = models.CharField('В том числе для кандидатов', max_length=256)
    inventory = models.CharField('Что получают работники', max_length=256)
    address = models.CharField('Адрес', max_length=256)
    description = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
