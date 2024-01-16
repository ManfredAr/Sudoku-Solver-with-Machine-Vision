import copy
import json
from django.http import JsonResponse
from django.shortcuts import render
from backend.killerSudokuGenerator import killerSudokuGenerator
from backend.SudokuTechniques.KillerSudokuHints import KillerSudokuHints

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
    

def genKillerSudoku(request):
    if request.method == "POST":
        gen = killerSudokuGenerator()
        puzzle, cages = gen.generate(request.POST.get("difficulty"))
        emptyGrid = copy.deepcopy(puzzle)
        for i in range(len(puzzle)):
            puzzle[i] = [str(x) if x != 0 else '-' for x in puzzle[i]]
            emptyGrid[i] = [str(x) if x == 0 else '-' for x in emptyGrid[i]]
        return JsonResponse({'grid': emptyGrid, "cages":cages, "solution" : puzzle})
    

def giveHint(request):
    if request.method == "POST":
        grid = json.loads(request.POST.get("grid"))
        cage = json.loads(request.POST.get("cage"))
        obj = KillerSudokuHints(grid, cage)
        hints = obj.getNextHint()
        if hints == -1:
            return JsonResponse({'hint': "Found through backtracking", 'answer': -1})
        return JsonResponse({'hint': hints[:-1], 'answer':hints[-1]})
