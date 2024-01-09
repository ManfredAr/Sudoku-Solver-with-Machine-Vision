from django.urls import path
from . import views

urlpatterns = [
    path('', views.playKillerSudoku),
    path('generatePuzzle/', views.genKillerSudoku)
]
