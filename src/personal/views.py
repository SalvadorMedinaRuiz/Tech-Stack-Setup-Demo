from django.shortcuts import render

# Create your views here.
#context = {}
#context['name'] = "Placeholder"
list_of_names = []

def home_screen_view(request):
    return render(request, "base.html", {}) #<-- {} for database variables

def view1(request):
    username = request.POST.get('name')
    if username != None:
        list_of_names.append(username)
    context = {'username':username, 'list_of_names':list_of_names}
    return render(request, "view1.html", context) #<-- {} for database variables

def view2(request):
    context = {'list_of_names':list_of_names}
    return render(request, "view2.html", context) #<-- {} for database variables