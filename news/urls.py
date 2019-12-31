from django.urls import path
from .views import scrape,news_list

urlpatterns = [
    path('home/', news_list),
    path('scrape/', scrape),
    
]