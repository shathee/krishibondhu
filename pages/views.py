from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home_view(request, *args, **kwargs):
	print (args, kwargs)
	return render(request, 'pages/home.html')


@api_view(['GET'])
def home_api_view(request):
	data = {'data':'This is home page'}
	return Response(data)

def about_view(request, *args, **kwargs):
	print (args, kwargs)
	return render(request, 'pages/about.html')

@api_view(['GET'])
def about_api_view(request):
	data = {'data':'This is about page'}
	return Response(data)

def contact_view(request, *args, **kwargs):
	print (args, kwargs)
	return render(request, 'pages/contact.html')

# def dashboard(request):
#     return render(request, 'pages/dashboard.html')

def login_view(request, *args, **kwargs):
	print (args, kwargs)
	return render(request, 'pages/login.html')

class LoginView(FormView):
    """ login view"""
    template_name = 'pages/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('profiles:dashboard')

    def form_valid(self, form):
        post_data = form.cleaned_data
        user = authenticate(username=post_data['username'],
                            password=post_data['password'])
        if user is not None:
            login(self.request, user)
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials.\
                    Please try again with correct input')
            return HttpResponseRedirect(reverse_lazy('pages:login'))

        return HttpResponseRedirect(reverse_lazy('profiles:dashboard'))

class SignupView(FormView):
    template_name = 'pages/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('profiles:dashboard')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()

        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())

def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect(reverse_lazy('profiles:dashboard'))