from django.shortcuts import render ,redirect
import requests
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def hug(request):
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    r = requests.get(url)
    fish = r.json()
    print(fish)
    # return fish
    context = {'queryset': fish}
    return render(request,'hug.html',context)

def logout_page(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('/login/')  
    

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in.")
            # Redirect to a success page or home page after login                            
            return redirect('/') # Adjust the redirect URL as needed
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login/') # Redirect back to the login page with error message
        
    return render(request, 'login.html')
def sign_up(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "Username Already Exist.")
            return redirect('/sign_up/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )

        messages.success(request, "Account created successfully.")
        # Render the same page to display the success message
        return render(request, 'sign_up.html')
    return render(request, 'sign_up.html')

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
    queryset = Receipe.objects.all()
    if request.GET.get('search_re'):
        queryset = queryset.filter(receipe_name__icontains =request.GET.get('search_re'))
        print(queryset)

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
