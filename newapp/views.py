from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {'mem':mem})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lasttname = request.POST['lasttname']
        country = request.POST['country']

        mem=Member(
            firstname=firstname, 
            lasttname=lasttname, 
            country=country)
        mem.save()
        return redirect("/")
    
def delete(request, id):
    mem=Member.objects.get(id=id)
    mem.delete()
    return redirect('/')

def update(request, id):
    mem = Member.objects.get(id=id)
    return render(request, 'update.html', {'mem':mem})

def uprec(request, id):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lasttname = request.POST['lasttname']
        country = request.POST['country']
        mem=Member.objects.get(id=id)

        mem.firstname=firstname
        mem.lasttname=lasttname
        mem.country=country
        mem.save()
        return redirect("/")