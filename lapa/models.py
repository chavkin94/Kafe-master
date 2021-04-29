from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from kafe import settings


class TipTovara(models.Model):
    class Meta:
        verbose_name = 'Тип Товарв'
        verbose_name_plural = 'Типы товара'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nazvanie


class Tovar(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)
    opisanie = models.TextField('Описание', null=True, blank=True)
    cena = models.FloatField('Цена', default=0)
    prevyu = models.ImageField('Превью', null=False, blank=False)
    tip_tovara = models.ForeignKey(TipTovara, verbose_name='Тип товара', on_delete=models.SET_NULL, related_name='tovari_set', null=True)
    kolvo_dobavlenia_v_korzinu = models.IntegerField('Кол-во раз добавили в корзину', default=0)

    def __str__(self):
        return self.nazvanie


class Akzia(models.Model):
    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    nazvanie = models.CharField(verbose_name='Название', max_length=255, null=False, blank=False)

    def __str__(self):
        return self.nazvanie


class Zakaz(models.Model):
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    telephone = models.CharField(max_length=30, null=True, blank=True, verbose_name='Телефон')
    fio = models.CharField('ФИО', max_length=255, null=True, blank=True)
    akzia = models.ForeignKey(Akzia, verbose_name='Акция', null=True, blank=True, on_delete=models.SET_NULL)
    data_i_vremia_zakaza = models.DateTimeField('Время заказа', auto_now_add=True, editable=False)
    adres = models.CharField('Адрес', max_length=255, null=True, blank=True, )
    status_zakaza = models.IntegerField(verbose_name='Статус заказа', choices=(
        (1, 'Оплачено'),
        (2, 'В пути'),
        (3, 'Выдано'),
    ))

    def __str__(self):
        return f'#{self.id}'



class DetaliZakaza(models.Model):
    class Meta:
        verbose_name = 'Деталь заказа'
        verbose_name_plural = 'Детали заказа'

    zakaz = models.ForeignKey(Zakaz, verbose_name='Заказ', on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovar, verbose_name='Товар', null=True, blank=True, on_delete=models.SET_NULL)
    stoimost_na_moment_realizazii = models.FloatField('Цена на момент реализации', null=True, blank=True)


class Sotrudnic(models.Model):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    user = models.OneToOneField(User, verbose_name='Логин', on_delete=models.CASCADE)
    telephone = models.CharField('Tелефон', null=True, blank=True, max_length=255)
    data_rozdenia = models.DateField('Дата рождения', null=True, blank=True)



class Otzivi(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


    avtor = models.CharField('Автор', max_length=255)
    otziv = models.TextField('Отзыв')
    telephone_avtora = models.CharField('Телефон автора', max_length=255)
    data_otziva = models.DateTimeField('Дата', auto_now_add=True)
    prosli_moderaziu = models.BooleanField('Модерацию прошли', default=False)

    def get_short_opisanie(self):
        return self.otziv[0:100]

    def __str__(self):
        return  f'{self.avtor}: {self.otziv[0:100]}...'

