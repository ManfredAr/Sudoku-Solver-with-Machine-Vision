import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.puzzleExtraction import PuzzleExtraction
from backend.KillerSudokuExtraction import KillerSudokuExtraction
from backend.convertToPuzzle import convertToPuzzle


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
    c = convertToPuzzle(grid, None)
    grid, solution = c.validateSudoku()
    if solution == False:
        return HttpResponse("incorrect puzzle", status=400)

    request.session['Sarray'] = grid
    request.session['Ssolution'] = solution
    return JsonResponse({'message': "sudoku"});


def playkillersudoku(request):
    grid = json.loads(request.POST.get("puzzle"))
    cage = json.loads(request.POST.get("cages"))
    c = convertToPuzzle(grid, cage)
    grid, new_cage, solution = c.validateKSudoku()
    if solution == False:
        return HttpResponse("incorrect puzzle", status=400)

    request.session['Sarray'] = grid
    request.session['Scage'] = json.dumps(new_cage)
    request.session['Ssolution'] = solution
    return JsonResponse({'message': "Ksudoku"});