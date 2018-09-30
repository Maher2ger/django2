from django.shortcuts import render
from django.http import HttpResponse




def index(request):
    my_dict = {'insert_me':"hallo, I am from views.py !!!",'welcome_massage':" Welcome in my first project ILESTA"}
    return render(request,'firstApp/index.html',context=my_dict)
