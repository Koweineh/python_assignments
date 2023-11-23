from django.urls import path
from . import views

urlpatterns = [
    path('form',views.display_form),
    path('route1',views.handle_form),
    path('show_results', views.show),
]
   