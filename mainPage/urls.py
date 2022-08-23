from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('god', views.home),
    path('card', views.home),
    path('partner', views.home),
    path('trio', views.home),
    path('dual', views.home),

]