from django.shortcuts import render

# Create your views here.
def playKillerSudoku(request):
    # retrieving the saved killer sudoku puzzle information
    try:
        grid = request.session['Sarray']
        cages = request.session['Scage']
        solution = request.session['Ssolution']
        request.session.clear()
        return render(request, "playkillersudoku/KSudoku.html", {"grid":grid, "cages":cages, "solution":solution})
    except:
        return render(request, "playkillersudoku/KSudoku.html", {"grid":-1, "cages":-1, "solution":-1})