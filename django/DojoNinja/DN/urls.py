from django.urls import path
from . import views
urlpatterns = [
    path("",views.method1),
    path("addDojo",views.method2),
    path("addNinja",views.method3)
]
