from django.urls import path
from . import views

#url cong
urlpatterns = [
    path('hello/', views.say_hello)
]
