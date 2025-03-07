from django.urls import path
from recipes.views import home, contato, sobre


urlpatterns = [
    path('sobre/', sobre),
    path('', home),
    path('contato/', contato),
]