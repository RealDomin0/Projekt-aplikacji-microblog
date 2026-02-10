from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

User = get_user_model()


def register(request):
    """Rejestracja nowego użytkownika."""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Konto zostało utworzone pomyślnie!')
            return render(
                request,
                'account/register_done.html',
                {'new_user': new_user},
            )
    else:
        user_form = UserRegistrationForm()
    
    return render(
        request,
        'account/register.html',
        {'user_form': user_form}
    )


@login_required
def edit_profile(request):
    """Edycja profilu zalogowanego użytkownika."""
    profile = request.user.profile
    
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user,
            data=request.POST
        )
        profile_form = ProfileEditForm(
            instance=profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profil został zaktualizowany!')
            return redirect('edit_profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    
    return render(
        request,
        'account/edit_profile.html',
        {
            'user_form': user_form,
            'profile_form': profile_form
        }
    )


def profile_detail(request, username):
    """Wyświetlanie profilu użytkownika."""
    user_obj = get_object_or_404(User, username=username)
    profile = user_obj.profile
    is_owner = request.user.is_authenticated and request.user == user_obj
    
    return render(
        request,
        'account/profile_detail.html',
        {
            'user_obj': user_obj,
            'profile': profile,
            'is_owner': is_owner,
        }
    )