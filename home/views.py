from django.shortcuts import render
from django.http import HttpResponse
from os import path
from django.conf import settings
from . models import contact

# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request, "about.html")

def download_cv(request):
    # Access the media_root directory from settings and join the path with pdf
    # to open the file, read as binary(bcoz it's pdf) and return in HttpResponse

    with open(path.join(settings.MEDIA_ROOT, "cv/ShivamResume.pdf"), "rb") as pd:
        response = HttpResponse(pd.read(), content_type="application/pdf")
        response[
            "Content-Disposition"
        ] = "attachment; filename=ShivamResume.pdf"
        return response

def contact_view(request):
        return render(request,'contact.html')


def send_view(request):
    if request.method=='POST':
        name=request.POST['Name'] 
        email=request.POST['Email'] 
        mobile=request.POST['Phone'] 
        msg=request.POST['txtMsg'] 
        contact(Name=name,Email=email,Mobile=mobile,Msg=msg).save()
        return render(request,'contact.html')

    else:
        return HttpResponse("<h1>404 - Not found </h1>")
   
def work_view(request):
    return render(request,'work.html')

def skill_view(request):
    return render(request,'skill.html')