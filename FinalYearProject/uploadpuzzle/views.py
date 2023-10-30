from django.http import JsonResponse
from django.shortcuts import render
from backend.puzzleExtraction import PuzzleExtraction
from backend.KillerSudokuExtraction import KillerSudokuExtraction
import cv2

# Create your views here.
def uploadPage(request):
    return render(request, "uploadpuzzle/upload.html", {})


def getPuzzle(request):
    if request.method == "POST":
        image = request.FILES['image'] 
        if request.POST.get("type") == "sudoku":
            converter = PuzzleExtraction(image)
            response = converter.ConvertToArray()
            print(response)
            for i in range(len(response)):
                response[i] = [str(x) if x != 0 else '-' for x in response[i]]
            return JsonResponse({'message': response, 'type': 'sudoku'})
        else:
            converter = KillerSudokuExtraction(image)
            grid, cages = converter.ConvertToPuzzle()
            return JsonResponse({'grid': grid, 'cages': cages, 'type':'Ksudoku'})
    return JsonResponse({'message': "success"});