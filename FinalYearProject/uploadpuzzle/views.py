import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from backend.puzzleExtraction import PuzzleExtraction
from backend.KillerSudokuExtraction import KillerSudokuExtraction
from backend.convertToSudoku import convertToSudoku


# Create your views here.
def uploadPage(request):
    return render(request, "uploadpuzzle/upload.html", {})


def getPuzzle(request):
    if request.method == "POST":
        image = request.FILES['image'] 
        if request.POST.get("type") == "sudoku":
            converter = PuzzleExtraction(image)
            response = converter.ConvertToArray()
            for i in range(len(response)):
                response[i] = [str(x) if x != 0 else '-' for x in response[i]]
            return JsonResponse({'message': response, 'type': 'sudoku'})
        else:
            converter = KillerSudokuExtraction(image)
            grid, cages = converter.ConvertToPuzzle()
            return JsonResponse({'grid': grid, 'cages': cages, 'type':'Ksudoku'})
    return JsonResponse({'message': "success"});



def playsudoku(request):
    grid = json.loads(request.POST.get("puzzle"))
    c = convertToSudoku(grid)
    grid, solution = c.validatePuzzle()
    if solution == False:
        return JsonResponse({'message': "failure"});

    request.session['Sarray'] = grid
    request.session['Ssolution'] = solution
    return JsonResponse({'message': "sudoku"});
