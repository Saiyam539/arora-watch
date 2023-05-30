from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages


# Superuser sam sam123
# Create your views here.
def index(request):
    return render(request,'index.html')

def signinuser(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if request.method=='POST':
            User.objects.create_user(username,email,password)
            messages.success(request,f'Account created Successfully ')
            return redirect('/loginuser')
    except Exception as e:
        messages.error(request, "Username already exists. Please choose a different username.")
    return render(request,'signin.html')


def loginuser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method=='POST':
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'You are now loged in')
            return redirect('/viewproduct')
        
        else:
            messages.success(request,f'Username or password is incorrect')
            return render(request,'login.html') 
        
    return render(request,'login.html')

def view_product(request):
    brand = Brand.objects.all()
    num_of_brand = brand.count()

    context = {
        'brands':brand,
        'num_of_brand':num_of_brand,
        'user':request.user
    }
    
    return render(request,'view_product.html',context)

def view_watches(request,id):
    brand = Brand.objects.get(id=id)
    watches = Brand_watch.objects.filter(brand=brand)
    
    context = {
        'brand':brand,
        'watches':watches
    }
    return render(request,'view_watch.html',context)