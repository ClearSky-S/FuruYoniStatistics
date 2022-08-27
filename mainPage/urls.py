from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('god', views.god),
    path('god/<slug:sort_by>', views.god),

    path('card', views.card_god_select),
    path('card/<slug:god_code>', views.card),

    path('partner', views.partner_god_select),
    path('partner/<slug:god_code>', views.partner),
    path('partner/<slug:god_code>/<slug:sort_by>', views.partner),

    path('trio', views.trio_god_select_1),
    path('trio/<slug:god_code_1>', views.trio_god_select_2),
    path('trio/<slug:god_code_1>/<slug:god_code_2>/<slug:sort_by>', views.trio),

    path('duel', views.dual),
    path('duel/<int:dual_id>', views.decklist),

]