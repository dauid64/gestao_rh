from .views import home, celery
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('celery/', celery, name='celery')
]
