from django.urls import path
from myapp.views import *
urlpatterns = [
    path('create/', create, name='create')
]