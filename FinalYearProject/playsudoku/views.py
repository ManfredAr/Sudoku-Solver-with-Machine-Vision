from django.shortcuts import render

# Create your views here.
def playSudoku(request):
    grid = request.session['Sarray']
    solution = request.session['Ssolution']
    return render(request, "playsudoku/playsudoku.html", {"grid":grid, "solution":solution})