from django.urls import path
from . import views

urlpatterns = [
    path('add_client', views.AddClient.as_view()),
    path('all_clients', views.AllClients.as_view()),
    path('add_mailing', views.AddMailing.as_view()),
    path('all_mailings', views.AllMailings.as_view()),
    path('all_messages', views.AllMessages.as_view()),
    path('test', views.test_celery),
]
