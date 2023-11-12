from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from app.forms import AddForm, LoginForm, SignupForm
from app.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()
   
    return render(request,"home.html",{'posts':posts})

def signuppage(request):
    if request.method == "POST": 
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
        else:
            return redirect("signuppage")
    else:
        form = SignupForm()
    return render(request,"signup.html",{'form':form})

def loginpage(request):
    if request.method == "POST":
        form = LoginForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("home")
            else:
                return redirect("loginpage")
    else:
        form = LoginForm()
    return render(request,"login.html",{'form':form})

def addpost(request):
    if request.method == "POST":
        form = AddForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = AddForm()
    return render(request,"addpost.html",{'form':form})

def updatepage(request,id):
    if request.method == "POST":
        post = Post.objects.get(id=id)
        form = AddForm(request.POST,request.FILES,instance=post)
        if form.is_valid:
            form.save()
            return redirect("home")
    else:
        post = Post.objects.get(id=id)
        form = AddForm(instance=post)

    return render(request,"update.html",{'form':form})