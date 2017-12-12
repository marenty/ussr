from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import *

def services(request):
    services = SeDict.objects.all()
    context = {'services': services}
    return render(request, 'services/services.html', context)
