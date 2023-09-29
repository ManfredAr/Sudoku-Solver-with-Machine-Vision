from django.shortcuts import render

# Create your views here.
def playKillerSudoku(request):
    return render(request, "playkillersudoku/KSudoku.html", {})