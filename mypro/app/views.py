from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import  HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Watch
from .forms import WatchForm
# Create your views here.



def index(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'index.html',data)

def details(request,watch_id):
    watch=Watch.objects.get(id=watch_id)
    return render(request,'details.html',{'watch':watch})

# def add_watch(request):
#     if request.method=='POST':
#         name=request.POST.get('name')
#         price = request.POST.get('price')
#         brand = int(request.POST.get('brand'))
#         img = request.FILES['image']
#         print(img)
#         watch=Watch(name=name,price=price,brand=brand,img=img)
#         watch.save()
#     return render(request,'add.html')

# def update(request,id):
#     watch = get_object_or_404(Watch, id=id)
#     if request.method=='POST':
#             name=request.POST.get('name')
#             price=request.POST.get('price')
#             brand=request.POST.get('brand')
#             img=request.FILES['image']
#             imgname=str(img)
#             watch.img.save(imgname, img, save=True)
#             Watch.objects.filter(id=id).update(name=name,price=price,brand=brand)
#             return  redirect('/')


    # return render(request,'edit.html',{'watch':watch})


# def delete(request,id):
#     if request.method=='POST':
#         deldata=Watch.objects.get(id=id)

#         deldata.delete()
#         return redirect('/')
#     return render(request,'delete.html')


# USER AUTHENTICATION PART
def register(request):
    if request.method=='POST':
        if request.method=='POST':
            username=request.POST.get('user_name')
            firstname = request.POST.get('first_name')
            lastname = request.POST.get('last_name')
            email= request.POST.get('email')
            pwd = request.POST.get('pwd')
            cnfpwd = request.POST.get('cnfpwd')
            if pwd==cnfpwd:
                if User.objects.filter(username=username).exists():
                    messages.info(request,"Username Already Exist")
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email Already Exist")
                    return redirect('/register')
                else:
                    user=User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email,password=pwd)
                    user.save()
                return redirect('/')
            else:
                messages.info(request, "Password Not Match")
                return redirect('/register')
    return render(request,'signup.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        user=auth.authenticate(username=username,password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Entry')
            return redirect('/login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def support(request):
    return render(request,'support.html')

def mec(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'mec.html',data)
def auto(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'auto.html',data)
def smt(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'smt.html',data)
def qur(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'qur.html',data)
def cro(request):
    content=Watch.objects.all()
    data={
        'result':content
    }
    return render(request,'cro.html',data)
def about(request):
    return render(request,'about.html')