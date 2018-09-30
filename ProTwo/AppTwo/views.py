from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<em> My second App </em>")

def help(request):
    my_dict = {'helpVar':"plz help me .. this page works"}
    return render(request,"AppTwo/help.html",context=my_dict)
