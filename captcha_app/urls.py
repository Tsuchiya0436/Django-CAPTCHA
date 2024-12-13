from django.urls import path, include
from .views import my_form_view, failure_view

urlpatterns = [
    path('', include('captcha.urls')),
    path('form/', my_form_view, name='my_form'),
    path('failure/', failure_view, name='failure'),
]
