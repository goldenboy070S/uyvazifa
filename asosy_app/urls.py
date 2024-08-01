from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='category'),
    path('post/<int:c_id>', post, name='post'),
]