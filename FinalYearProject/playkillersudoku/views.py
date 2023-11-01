from django.shortcuts import render

# Create your views here.
def playKillerSudoku(request):
    grid = request.session['Sarray']
    cages = request.session['Scage']
    solution = request.session['Ssolution']
    print(2)
    print(cages)
    return render(request, "playkillersudoku/KSudoku.html", {"grid":grid, "cages":cages, "solution":solution})