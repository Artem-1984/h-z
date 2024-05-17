from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from .forms import LoginUserForm
from django.urls import reverse

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['username'], password = cd['password'])
            if user :
                login(request, user)
                return HttpResponseRedirect(('/'))
    else:
        form = LoginUserForm()
    return render(request, 'login.html', {'form': form})

def login_out(request):
    logout(request)
    return HttpResponseRedirect(('/'))