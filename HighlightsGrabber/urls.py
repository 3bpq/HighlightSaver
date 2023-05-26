
from django.contrib import admin
from django.urls import path, include
from GetVideos import views

urlpatterns = [
    path('GetVideos/', views.get_name),
    path('admin/', admin.site.urls),
    path('Videos/', views.Videos)
]
