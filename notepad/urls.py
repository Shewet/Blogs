from django.urls import path
from .views import create_note,list_notes,delete_note,update_note

urlpatterns = [
    path('<int:id>/delete/',delete_note),
    path('<int:id>/update/',update_note),
    path('create/', create_note),
    path('list/',list_notes),
    
]