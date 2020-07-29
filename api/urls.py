from django.urls import path

from api.rest.views import get_fibonachi_slice

urlpatterns = [
    path('fibonachi/', get_fibonachi_slice, name='fibonachi_sequence'),
]

