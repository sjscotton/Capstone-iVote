from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('voter', views.show, name='show'),
    path('vote_dates', views.show_votes, name='show_votes'),
    path('address', views.get_addresses, name='get_addresses'),
    path('elections', views.get_elections, name='get_elections')
]
