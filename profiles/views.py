from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.

def dashboard(request):
    if(request.user.is_authenticated):
        return render(request, 'profiles/dashboard.html')
    else:
        return HttpResponseRedirect(reverse_lazy('pages:login'))
        