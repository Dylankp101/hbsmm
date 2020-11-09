from django.shortcuts import render, redirect
from .models import Client, Admin
from django.contrib import messages





def headpage(request):
    return render(request, "headpage.html")

def services(request):
    return render(request, "services.html")

def portfolio(request):
    return render(request, "portfolio.html")

def appointments(request):
    return render(request, "appointments.html")

def adduser(request):
    errors = Client.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect("/appointments")
    else:
        Client.objects.create(
        name=request.POST['name'], 
        email=request.POST['email'], 
        phone=request.POST['phone'], 
        date=request.POST['date'],
        time=request.POST['time'],
        notes=request.POST['notes'],
            )
    return redirect("/thankyou")

def login(request):
    return render(request, "login.html")

def signin(request):
    context={
        'clients':Client.objects.all(),
    }
    errors=Admin.objects.l_validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v, extra_tags = k)
        return redirect('/login')
    else:
        return render(request,'clients.html',context)

def logout(request):
    request.session.flush()
    return redirect('/')

def thankyou(request):
    return render(request, "thankyou.html")

def delete(request,id):
    if request.method == "GET":
        context={
            'clients':Client.objects.all()
        }
    Client.objects.get(id=id).delete()
    return render(request, 'clients.html', context)
    



