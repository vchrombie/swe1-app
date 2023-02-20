from django.shortcuts import render


def index(request):
    return render(request, 'swe1_app/index.html')