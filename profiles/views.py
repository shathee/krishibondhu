from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.db import transaction



from .forms import UserForm, ProfileForm
from .models import Profile

# Create your views here.

def dashboard(request):
    if(request.user.is_authenticated):
        return render(request, 'profiles/dashboard.html')
    else:
        return HttpResponseRedirect(reverse_lazy('pages:login'))


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('profiles:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    user = Profile.objects.get(user_id = request.user.id)
    # print(user.district.division)
    context = {
        'user_data': user,
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profiles/profile.html', context)