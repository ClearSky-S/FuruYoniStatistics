from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('god', views.god),
    path('card', views.card_god_select),
    path('card/<slug:god>', views.card),
    path('partner', views.partner_god_select),
    path('partner/<slug:god>', views.partner),

    path('trio', views.trio),
    path('dual', views.dual),

]