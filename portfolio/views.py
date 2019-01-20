from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys=Gallery.objects.all()
    print(type(gallerys))
    return render(request,"home.html",{'gallerys':gallerys})
