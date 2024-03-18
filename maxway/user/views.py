from django.shortcuts import render, redirect
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login
def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        print(form, form.is_valid())
        form.save()
        return redirect('sign_in')

    ctx = {
        'form': form
    }
    return render(request, 'signup.html', ctx)

def sign_in(request):
    form = SignInForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')

    ctx = {
        'form': form
    }
    return render(request, 'signin.html', ctx)