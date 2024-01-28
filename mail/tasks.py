from celery import shared_task
from mail import models
import time
import datetime as dt


@shared_task
def create_pending_messages(mailing_id):
    mailing = models.Mailing.objects.get(pk=mailing_id)

    recipients = models.Client.objects.filter(tag=mailing.filter)

    lower_date_time = dt.datetime.strptime(mailing.date_time_mailing.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    lower_date_time += dt.timedelta(hours=3)
    now_date_time = dt.datetime.now()

    second_difference = (lower_date_time - now_date_time).total_seconds()
    time.sleep(second_difference)

    for client in recipients:
        models.Message.objects.create(date_time_create=dt.datetime.now(), mailing=mailing, client=client)
        print(f'Письмо для клиента с id = {client.pk}: "{mailing.message_text}"')
