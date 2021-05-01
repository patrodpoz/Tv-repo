from django.urls import path, include
from . import views  
urlpatterns = [
    path('', views.shows),
    path('add_show', views.add_show),
    path('add', views.add),
    path('shows/<int:idShow>', views.view_show),
    path('shows/<int:idShow>/edit', views.edit_show),
    path('edit/<int:idShow>', views.edit),
    path('delete/<int:idShow>', views.delete),
]