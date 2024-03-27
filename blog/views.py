from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def blog(request):
    return render(request,'blog/blog.html')




def singleblog(request):
    return render(request,'blog/singleblog.html')


def singleblog1(request):
    return render(request,'blog/singleblog1.html')




