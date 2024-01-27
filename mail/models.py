from django.core.validators import RegexValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from .utils import create_massages


class Client(models.Model):
    phone = PhoneNumberField(verbose_name='Телефон', region='RU', unique=True)
    cod_phone = models.CharField(max_length=3, validators=[
        RegexValidator(regex='^[0-9]{3}$', message='Code must be 3 digits',
                       code='invalid_code')
    ], verbose_name='Код оператора')
    tag = models.CharField(max_length=25, verbose_name='Тег')

    def __str__(self):
        return f'Клиент. id = {self.pk}'


class Message(models.Model):
    date_time_create = models.DateTimeField(verbose_name='Дата отправки письма')
    mailing = models.ForeignKey('Mailing', related_name='mailing', on_delete=models.PROTECT, default=None,
                                verbose_name='Рассылка')
    client = models.ForeignKey(Client, related_name='client', on_delete=models.PROTECT, default=None,
                               verbose_name='Клиент')

    def __str__(self):
        return f'Письмо. id = {self.pk}'


class Mailing(models.Model):
    date_time_mailing = models.DateTimeField(verbose_name='Дата старта рассылки')
    message_text = models.TextField(verbose_name='Текст рассылки')
    filter = models.CharField(max_length=25, verbose_name='Фильтр')
    end_date_time_mailing = models.DateTimeField(verbose_name='Дата окончания рассылки')

    def __str__(self):
        return f'Рассылка. id = {self.pk}'

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save()
        create_massages(self)
