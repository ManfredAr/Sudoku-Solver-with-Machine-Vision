from django.shortcuts import render

# Create your views here.
def uploadPage(request):
    return render(request, "uploadpuzzle/upload.html", {})


def getPuzzle(request):
    return "yes"