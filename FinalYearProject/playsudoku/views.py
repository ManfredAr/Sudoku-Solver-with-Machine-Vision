import json
from django.http import JsonResponse
from django.shortcuts import render
from backend.SudokuGenerator import SudokuGenerator
from backend.SudokuTechniques.SudokuHints import SudokuHints

# Create your views here.
def playSudoku(request):
    '''
    If a Sudoku puzzle was stored then that puzzle is returned otherwise a new 
    puzzle will be returned.
    '''
    try:
        grid = request.session['Sarray']
        solution = request.session['Ssolution']
        request.session.clear()
        return render(request, "playsudoku/playsudoku.html", {"grid":grid, "solution":solution})  
    except:
        return render(request, "playsudoku/playsudoku.html", {"grid":-1, "solution":-1})
    

def genSudoku(request):
    if request.method == "POST":
        gen = SudokuGenerator()
        puzzle, solution = gen.generate(request.POST.get("difficulty"))
        for i in range(len(puzzle)):
            puzzle[i] = [str(x) if x != 0 else '-' for x in puzzle[i]]
            solution[i] = [str(x) if x != 0 else '-' for x in solution[i]]
        return JsonResponse({'grid': puzzle, "solution":solution})
    

def getHint(request):
    if request.method == "POST":
        grid = json.loads(request.POST.get("grid"))
        obj = SudokuHints(grid)
        hints = obj.getNextHint()
        if hints == -1:
            return JsonResponse({'hint': "Found through backtracking", 'answer': -1})
        return JsonResponse({'hint': hints[:-1], 'answer':hints[-1]})
