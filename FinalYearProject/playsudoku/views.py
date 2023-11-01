from django.shortcuts import render

# Create your views here.
def playSudoku(request):
    try:
        grid = request.session['Sarray']
        solution = request.session['Ssolution']
        request.session.clear()
        return render(request, "playsudoku/playsudoku.html", {"grid":grid, "solution":solution})  
    except:
        return render(request, "playsudoku/playsudoku.html", {"grid":-1, "solution":-1})