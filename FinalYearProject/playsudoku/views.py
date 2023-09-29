from django.shortcuts import render

# Create your views here.
def playSudoku(request):
    return render(request, "playsudoku/playsudoku.html", {})