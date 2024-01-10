from django.urls import path
from . import views

urlpatterns = [
    path('', views.playSudoku),
    path('generatePuzzle/', views.genSudoku),
    path('giveHint/', views.getHint)
]
