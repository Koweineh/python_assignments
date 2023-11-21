from django.urls import path
from .views import index, process_money,reset

urlpatterns = [
    path('', index ),
    path('process_money', process_money, ),
    path('reset',reset)
]
