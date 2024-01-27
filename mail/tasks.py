from datetime import datetime
from celery import shared_task
from mail import models
import time


@shared_task
def create_pending_messages(mailing):
    recipients = models.Client.objects.filter(tag=mailing.filter)

    lower_date_time = datetime.strptime(mailing.date_time_mailing.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    now_date_time = datetime.now()

    second_difference = (lower_date_time - now_date_time).total_seconds()
    time.sleep(second_difference)

    for client in recipients:
        models.Message.objects.create(date_time_create=datetime.now(), mailing=mailing, client=client)
        print(f'Письмо для клиента с id = {client.pk}: "{mailing.message_text}"')
