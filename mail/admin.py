from django.contrib import admin
from .models import Client, Message, Mailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'cod_phone', 'tag')


@admin.register(Message)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_create', 'mailing', 'client')
    readonly_fields = ('id', 'date_time_create', 'mailing', 'client')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_time_mailing', 'end_date_time_mailing', 'filter', 'message_text')
    readonly_fields = ('id', 'date_time_mailing', 'end_date_time_mailing', 'filter', 'message_text')
