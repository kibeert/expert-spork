from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.
def signupview(request, *args, **kwargs ):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect("articles")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def loginview(request, *args, **kwargs):
    if request.method =="POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return redirect("articles")  
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})
