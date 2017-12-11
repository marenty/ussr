from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from services.models import SeDict
import datetime
from company.sqlSelect import *
import json
from .models import *
from django.views.generic.list import ListView

def index(request):
    """Strona główna dla aplikacji ussr."""
    return render(request, 'company/index.html')

# def calGenListView(ListView):


def generate_calendar(request):

    #service = SeDict.objects.get(id_se_dict = "WOPO")
    #date_start = datetime.now()
    #date_finish = date_start + datetime.timedelta(days = 7)

    result = gen_calendar()
    
    # listResult = gen_calendar()
    # result = json.dumps(listResult)
    # result = '/n'.join(record in listResults)
    return render(request, 'company/calendar_test.html', {'result' : result})
#    return HttpResonse(result, content_type = "application/json")

# def add(request):
#     sqlResult = sqlSelect()
#     return render(request, 'company/sql.html', {'queryResult': sqlResult})
