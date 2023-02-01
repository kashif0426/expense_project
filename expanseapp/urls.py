from django.urls import path
from .views import * 

urlpatterns = [
    path('expense', expense),
    path('del/<int:id>', del_views, name = "del")
]
