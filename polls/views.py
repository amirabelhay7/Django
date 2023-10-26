from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    backvar="Amira Belhay"
    context={"frontvar": backvar , "var1":7}
    return render(request, "index.html", context)