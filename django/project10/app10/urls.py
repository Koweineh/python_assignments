
from django.urls import path
from . import views

urlpatterns = [
    path('form',views.method1),
    path('handleform',views.method2),
    path('xxx',views.method3),
]