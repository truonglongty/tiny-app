from django.urls import path
from . views import *

urlpatterns = [
    path('', post_list, name='post-list'),
    path('post/<int:pk>/', post_detail, name='post-detail'),
]