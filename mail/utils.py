from datetime import datetime

from mail import models
from .tasks import create_pending_messages


def create_messages(mailing):
    recipients = models.Client.objects.filter(tag=mailing.filter)

    lower_date_time = datetime.strptime(mailing.date_time_mailing.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    now_date_time = datetime.now()
    upper_date_time = datetime.strptime(mailing.end_date_time_mailing.strftime('%Y-%m-%d %H:%M:%S'),
                                        '%Y-%m-%d %H:%M:%S')

    if lower_date_time < now_date_time < upper_date_time:
        for client in recipients:
            models.Message.objects.create(date_time_create=datetime.now(), mailing=mailing, client=client)
            print(f'Письмо для клиента с id = {client.pk}: "{mailing.message_text}"')

    if lower_date_time > now_date_time:
        create_pending_messages.delay(mailing_id=mailing.pk)
