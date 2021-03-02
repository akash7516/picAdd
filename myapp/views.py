from django.shortcuts import render
from .models import Image
from .forms import ImageForm

# Create your views here.
def Home(request):
    if request.method=="POST":
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    img=Image.objects.all()        
    form=ImageForm()
    return render(request,"home.html",{'img':img ,'form':form})
