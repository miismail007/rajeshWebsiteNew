

from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.blog,name='blog'),
    path('singleblog/',views.singleblog,name='singleblog'),
    path('singleblog1/',views.singleblog1,name='singleblog1'),
    
]
