from django.urls import path

from microhr.views import worker

urlpatterns = [
    path('', worker.resume, name='resume'),
]