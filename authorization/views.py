from django.contrib.auth.models import User
from django.shortcuts import render

from authorization.forms import RegisterUserForm


def register_view(request):

    form = RegisterUserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['login'],
                form.cleaned_data['email'],
                form.cleaned_data['password']
            )
            user.save()
    return render(
        request,
        'authorization/register.html',
        context={'form': form}
    )