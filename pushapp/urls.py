from django.urls import path

from .views import home, send_push

urlpatterns = [
    path('', home, name='home'),
    path('send_push', send_push, name='send_push'),
]
