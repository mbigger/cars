import os
from django.urls import path,include
from .views import *

urlpatterns = [
    path("",index,name="homepage"),
    path("quiz",quiz,name="quiz"),
]