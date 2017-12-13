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
from utilities.models import WorkdayCalendarParams


def index(request):
    """Strona główna dla aplikacji ussr."""
    return render(request, 'company/index.html')

# def calGenListView(ListView):


def generate_calendar(request):

    #service = SeDict.objects.get(id_se_dict = "WOPO")
    #date_start = datetime.now()
    #date_finish = date_start + datetime.timedelta(days = 7)
    workday_calendar = WorkdayCalendarParams.objects.get(id_workday_calendar_params = 1)

    week_workday_start = workday_calendar.default_workday_start_time
    week_workday_end = workday_calendar.default_workday_end_time

    saturday_workday_start = workday_calendar.default_saturday_start_time
    saturday_workday_end = workday_calendar.default_saturday_end_time

    if ( saturday_workday_start != None and saturday_workday_end != None):
        if (week_workday_start < saturday_workday_start):
            workday_start = week_workday_start
        else:
            workday_start = saturday_workday_start

        if (week_workday_end > saturday_workday_end):
            workday_end = week_workday_end
        else:
            workday_end = saturday_workday_end
    else:
        workday_start = week_workday_start
        workday_end = week_workday_end




    result = gen_calendar()

    context = {'result' : result,
                'workday_start' : workday_start,
                'workday_end' : workday_end,
                }
    # listResult = gen_calendar()
    # result = json.dumps(listResult)
    # result = '/n'.join(record in listResults)
    return render(request, 'company/calendar_test.html', context)
#    return HttpResonse(result, content_type = "application/json")

# def add(request):
#     sqlResult = sqlSelect()
#     return render(request, 'company/sql.html', {'queryResult': sqlResult})
