import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from backend.SudokuExtraction import SudokuExtraction
from backend.KillerSudokuExtraction import KillerSudokuExtraction
from backend.convertToPuzzle import convertToPuzzle


# Create your views here.
def uploadPage(request):
    return render(request, "uploadpuzzle/upload.html", {})


def getPuzzle(request):
    '''
    Receives an image from the frontend, converts the image to a 
    2D array and cages for killer Sudoku
    Returns:
    A puzzle if found and an error code otherwise
    '''
    if request.method == "POST":
        image = request.FILES['image'] 
        if request.POST.get("type") == "sudoku":
            converter = SudokuExtraction(image)
            response = converter.convertToArray()
            for i in range(len(response)):
                response[i] = [str(x) if x != 0 else '-' for x in response[i]]
            return JsonResponse({'message': response, 'type': 'sudoku'})
        else:
            converter = KillerSudokuExtraction(image)
            grid, cages = converter.convertToPuzzle()
            return JsonResponse({'grid': grid, 'cages': cages, 'type':'Ksudoku'})
    return HttpResponse("puzzle not found", status=400)



def playsudoku(request):
    '''
    Receives a Sudoku puzzle from frontend, checks if it is a valid puzzls.
    
    Returns:
    Success message if puzzle is valid and error message otherwise.
    '''
    grid = json.loads(request.POST.get("puzzle"))
    c = convertToPuzzle(grid, None)
    grid, solution = c.validateSudoku()
    if solution == False:
        return HttpResponse("incorrect puzzle", status=400)

    # storing the grid and solution in a sessions db table
    request.session['Sarray'] = grid
    request.session['Ssolution'] = solution
    return JsonResponse({'message': "sudoku"});


def playkillersudoku(request):
    '''
    Receives a killer Sudoku puzzle from frontend, checks if it is a valid puzzls.
    
    Returns:
    Success message if puzzle is valid and error message otherwise.
    '''
    grid = json.loads(request.POST.get("puzzle"))
    cage = json.loads(request.POST.get("cages"))
    c = convertToPuzzle(grid, cage)
    grid, new_cage, solution = c.validateKSudoku()
    if solution == False:
        return HttpResponse("incorrect puzzle", status=400)

    # storing the grid, cage and solution in a sessions db table
    request.session['Sarray'] = grid
    request.session['Scage'] = json.dumps(new_cage)
    request.session['Ssolution'] = solution
    return JsonResponse({'message': "Ksudoku"});