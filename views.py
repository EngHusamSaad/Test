
from django.shortcuts import render, HttpResponse,redirect
from dojo_ninjas_app.models import *

def index(request):
    
    data={
        "all_dojos":Dojo.objects.all(),
        "dojo_count": Dojo.objects.all().count,
        "ninja_count": Ninja.objects.all().count,
    }
    
    return render(request,"index.html",data)


def adddojo(request):
    if request.method == 'POST':
        name=request.POST["name"]
        city=request.POST["city"]
        state=request.POST["state"]
        new_dojo=Dojo.objects.create(name=name,city=city,state=state)
        
        # dojo_select = request.POST.get("dojo_select")
        
        # print(dojo_select)
        # print(request.POST)
        

    return redirect('/')


def addninja(request):
    first_name=request.POST["first_name"]
    last_name=request.POST["last_name"]
    dojo_select = request.POST["dojo_select"]
    dojo_user=Dojo.objects.get(name=dojo_select)
    new_ninja=Ninja.objects.create(first_name=first_name,last_name=last_name,dojo=dojo_user)
    
    print(dojo_select)
    return redirect('/')


def delete_user(request):
    dojo_delete=request.POST["dojo_id"]
    print(dojo_delete)
    dojo_user=Dojo.objects.get(id=int(dojo_delete))
    dojo_user.delete()
    
    return redirect('/')
    
    
