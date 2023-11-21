# formapp/urls.py
from django.urls import path
from .import views



urlpatterns = [
    path("",views.welcome),
    path('form', views.form_view),
    path('result', views.result_view),
     path('show_results', views.show),
]
