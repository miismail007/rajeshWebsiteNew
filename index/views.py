from django.shortcuts import render

from django.http import HttpResponse

from .models import blognew

from .models import contactform

from .models import portfolio_photos

from .models import experience

from .models import education

from .models import about as about2


def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        
        message=request.POST.get('message')

        contactformdata=contactform(name=name,email=email,message=message)
        contactformdata.save()
        
    blognewdata=blognew.objects.all().order_by('-date123')
    portfolio_photosdata=portfolio_photos.objects.all().order_by('-id')
    experiencedata=experience.objects.all().order_by('-id')
    educationdata=education.objects.all().order_by('-id')
    aboutdata2=about2.objects.all().order_by('id')
    context={
        'blognew':blognewdata,
        'portfolio_photos':portfolio_photosdata,
        'about2':aboutdata2,
        'experience':experiencedata,
        'education':educationdata


    }


    return render(request,'layouts.html',context)




def blogpage(request):
    blognewdata=blognew.objects.all().order_by('-date123')

    context1={
        'blognew':blognewdata,
        


    }
    return render(request,'blogpage.html',context1)

def about(request):
    return render(request,'about.html')


def resume(request):
    return render(request,'resume.html')

def portfolio(request):
    return render(request,'portfolio.html')

def contact(request):
    return render(request,'contact.html')