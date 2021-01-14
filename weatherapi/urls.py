from django.urls import path
from .views import IndexView

app_name = 'weatherapi'

urlpatterns = [
    path('', IndexView, name='index')
]

