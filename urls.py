from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('save-location/', views.save_locations, name='save_location'),
    path('places/<int:location_id>', views.show_places, name='show_places'),
]