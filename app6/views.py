from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage

# Create your views here.

def base(request):
    return render(request,"base.html")

def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        phonenumber=request.POST.get("phone number")
        gender=request.POST.get("gender")
        DOB=request.POST.get("DOB")
        language=request.POST.getlist("language")
        coding=request.POST.getlist("coding")
        send_mail("thanks for registration","hello {} {}\n thanks for registering ".format(first_name,last_name),
        "roopendrark@gmail.com",[email,],fail_silently=False)
        return HttpResponse("{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>{}<br>".format(first_name,last_name,email,password,phonenumber,gender,DOB,language,coding))
    return render(request,"app6/registration.html")
    

def img_upld(request):
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        fs=FileSystemStorage()
        fs.save(image.name,image)
    return render(request,"img_upld.html")
