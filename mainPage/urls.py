from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('god', views.god),
    path('card', views.card),
    path('partner', views.partner),
    path('trio', views.trio),
    path('dual', views.dual),

]