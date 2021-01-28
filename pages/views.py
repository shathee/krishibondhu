from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ProfileForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template.response import TemplateResponse
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from profiles.models import Profile
from general.models import District


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
                    Please try again with correct input', extra_tags='alert alert-warning')
            return HttpResponseRedirect(reverse_lazy('pages:login'))

        return HttpResponseRedirect(reverse_lazy('profiles:dashboard'))

# class SignupView(FormView):
#     template_name = 'pages/signup.html'
#     form_class = SignupForm
#     success_url = reverse_lazy('profiles:dashboard')
    
#     def form_valid(self, form):
        
#         user = form.save(commit=False)
       
#         user.set_password(form.cleaned_data['password'])
#         user.is_active = True
#         user.save()
#         login(self.request, user)

#         return HttpResponseRedirect(self.get_success_url())

# def signup_view(request):
# 	if request.method == 'POST':
# 		signup_form = SignupForm(request.POST)
# 		profile_form = ProfileForm(request.POST)
# 		if signup_form.is_valid() and profile_form.is_valid():
# 			signup_form.cleaned_data['password']=make_password(signup_form.cleaned_data['password'])
# 			user = signup_form.save()
# 			user_id = user.id
# 			update_data = profile_form.cleaned_data

# 			print(update_data['district'])
# 			Profile.objects.filter(user_id=user_id).update(**update_data)
# 			username = signup_form.cleaned_data.get('username')
# 			raw_password = signup_form.cleaned_data.get('password')
# 			# user = authenticate(username=username, password=raw_password)
# 			login(request, user)
# 			return redirect('/dashboard')
# 	else:
# 		signup_form = SignupForm()
# 		profile_form = ProfileForm()
# 	return render(request, 'pages/signup.html', {'signup_form': signup_form, 'profile_form':profile_form})

def signup_view(request):
	if request.method == 'POST':
	    signup_form = SignupForm(request.POST)
	    profile_form = ProfileForm(request.POST)
	    if signup_form.is_valid() and profile_form.is_valid():
	    	user = signup_form.save(commit=False)
	    	user.password=make_password(signup_form.cleaned_data['password'])
	    	user.save()
	    	user.refresh_from_db()
	    	profile_form = ProfileForm(request.POST, instance=user.profile)
	    	profile_form.full_clean()
	    	profile_form.save()
	    	messages.add_message(request, messages.SUCCESS, f'Your account has been created!', extra_tags='alert alert-success')
	    	# messages.success(request, f'Your account has been created!')
	    	return redirect('/dashboard')
	else:
	    signup_form = SignupForm()
	    profile_form = ProfileForm()
	context = {
	    'signup_form': signup_form,
	    'profile_form': profile_form
	}
	return render(request, 'pages/signup.html', context)

def Logout(request):
    """logout logged in user"""
    logout(request)
    return redirect(reverse_lazy('profiles:dashboard'))
