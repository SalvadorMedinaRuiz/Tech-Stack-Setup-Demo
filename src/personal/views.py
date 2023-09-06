from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    print(request.headers)
    return render(request, "base.html", {}) #<-- {} for database variables

def view1(request):
    print(request.headers)
    return render(request, "view1.html", {}) #<-- {} for database variables