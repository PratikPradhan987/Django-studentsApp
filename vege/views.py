from django.shortcuts import render ,redirect
from .models import *
# Create your views here.
def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        print("receipe_image",receipe_image)
        print(data)
        Receipe.objects.create(
            receipe_name = data['receipe_name'],
            receipe_description = data['receipe_description'],
            receipe_image = receipe_image,            
            )
        return redirect('/')

    return render(request,'receipes.html')