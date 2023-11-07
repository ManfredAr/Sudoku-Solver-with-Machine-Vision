from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadPage),
    path('uploadImage/', views.getPuzzle),
    path('loadSudoku/', views.playsudoku),
    path('loadKSudoku/', views.playkillersudoku),
]
