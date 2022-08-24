from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('god', views.god),
    path('card', views.card_god_select),
    path('card/<slug:god>', views.card),
    path('partner', views.partner_god_select),
    path('partner/<slug:god>', views.partner),

    path('trio', views.trio_god_select_1),
    path('trio/<slug:god1>', views.trio_god_select_2),
    path('trio/<slug:god1>/<slug:god2>', views.trio),

    path('dual', views.dual),
    path('dual/<int:number>/<int:isWinner>', views.decklist),

]