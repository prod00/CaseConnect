from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from case_connecting.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUPdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            form.save()
            messages.success(request, f'Welcome, {first_name}! Your account has successfully been created. You are now '
                                      f'able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUPdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile,)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUPdateForm(instance=request.user.profile)

    username = request.user.username
    context = {
        'u_form': u_form,
        'p_form': p_form,
        # either make usernames unique or change this to email and make email required

    }

    return render(request, 'users/profile.html', context)

