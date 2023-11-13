from django.shortcuts import render

def playKillerSudoku(request):
    '''
    Returns a killer Sudoku puzzle if saved in the session table otherwise a new
    puzzle is returned.
    '''
    try:
        grid = request.session['Sarray']
        cages = request.session['Scage']
        solution = request.session['Ssolution']
        request.session.clear()
        return render(request, "playkillersudoku/KSudoku.html", {"grid":grid, "cages":cages, "solution":solution})
    except:
        return render(request, "playkillersudoku/KSudoku.html", {"grid":-1, "cages":-1, "solution":-1})