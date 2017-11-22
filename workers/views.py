from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test





def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('MainPage:index'))


def is_logged_employee(user):
    if user is not None:
        return user.groups.filter(name='workers').exists()

@user_passes_test(is_logged_employee, login_url = '/employee/login', redirect_field_name = None)
def employee_main(request):
    return  render(request, 'workers/index.html')


def employee_login(request):
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
        username = form.data['username']
        password = form.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.groups.filter(name='workers').exists():
                login(request, user)
                return HttpResponseRedirect(reverse('workers:employee_main'))
            else:
                return render(request, 'workers/login.html', {'form': form,
                                                            'invalid': True})

    return render(request, 'workers/login.html', {'form': form})
