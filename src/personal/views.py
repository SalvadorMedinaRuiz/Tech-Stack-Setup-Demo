from django.shortcuts import render
from .models import Persons
# Create your views here.
#context = {}
#context['name'] = "Placeholder"
#list_of_names = []

def home_screen_view(request):
    return render(request, "base.html", {}) #<-- {} for database variables

def view1(request):
    if request.method == 'POST':
        post = Persons()
        post.name = request.POST.get('name')
        post.save()
    
    latest_person = Persons.objects.latest('id')

    context = {'latest_person':latest_person}
    return render(request, "view1.html", context) #<-- {} for database variables
    #username = request.POST.get('name')
    #if username != None:
    #    list_of_names.append(username)
    #context = {'username':username, 'list_of_names':list_of_names}
    #return render(request, "view1.html", context) #<-- {} for database variables

def view2(request):
    list_of_names = []
    all_persons = Persons.objects.all
    for item in all_persons():
        if item.name != None:
            list_of_names.append(item.name)
    context = {'list_of_names':list_of_names}
    return render(request, "view2.html", context) #<-- {} for database variables