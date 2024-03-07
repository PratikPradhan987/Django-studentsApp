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
    
def delete_receipe(request,id):
    print(id)
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/')

def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name'),
        receipe_description = data.get('receipe_description'),
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/')

    context = {'queryset': queryset}
    return render(request,'update_receipes.html',context)
