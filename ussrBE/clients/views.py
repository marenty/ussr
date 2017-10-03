# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import ClBlockedReasonDict
from .sqlSelect import sqlSelect

def index(request):
    plannedServicesList = ClBlockedReasonDict.objects.order_by('id_cl_blocked_reason_dict')[:5]
    # template = loader.get_template('clients/index.html')
    context = {
        'plannedServicesList': plannedServicesList,
    }
    # output = ', '.join([s.blocked_reason_name for s in testList])
    # return HttpResponse(template.render(context, request))
    return render(request, 'clients/index.html', context)

def detail(request, blockedReason):
    # response = "dupa %s"
    # return HttpResponse(response % sth)
    blockedReasonX = get_object_or_404(ClBlockedReasonDict, pk=blockedReason)
    return render(request, 'clients/detail.html', {'blockedReason': blockedReasonX})

def add(request):
    sqlResult = sqlSelect()
    return render(request, 'clients/sql.html', {'queryResult': sqlResult})
