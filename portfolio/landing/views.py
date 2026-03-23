from django.shortcuts import render

# Create your views here.
def español(request):
    return render(request, 'español.html')

def english(request):
    return render(request, 'ingles.html')