from django.urls import path
from .views import * 

urlpatterns = [
    path('expense', expense, name = "expense"),
    path('del/<int:id>', del_views, name = "del"),
    path('edit/<int:id>', edit_views, name = "edit"),
]
