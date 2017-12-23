from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.urlresolvers import reverse
from services.models import SeDict
import time
import datetime
from company.sqlSelect import *
import json
from .models import *
from clients.models import Client
from services.models import SeDict, SeGroupDict
from machines.models import Machine
from workers.models import Worker
from company.models import Location
from django.views.generic.list import ListView
from utilities.models import WorkdayCalendarParams, ResourcesUsage, WorkdayCalendar
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm

def services(request):
    services = SeDict.objects.all()
    context = {'services': services}
    return render(request, 'services/services.html', context)


def index(request):
    """Strona główna dla aplikacji ussr."""
    return render(request, 'company/index.html')

# def calGenListView(ListView):

def generate_summary(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            service = SeDict.objects.get(id_se_dict = reservation_form.cleaned_data['service'])
            datetime = reservation_form.cleaned_data['date']

        context = {'service' : service,
                   'datetime' : datetime}

    return render(request, 'services/reservation_summary.html', context)

def get_resources_to_reservation(result):
    free_worker = result.free_workers[0]
    free_machine = result.free_machines[0]
    free_location = result.free_locations[0]
    resources = {'free_worker' : free_worker,
                'free_machine' : free_machine,
                'free_location' : free_location }

    return resources

def save_reservation(request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            service_id = SeDict.objects.get(id_se_dict = reservation_form.cleaned_data['service'])
            date_time = reservation_form.cleaned_data['date']
            facture = reservation_form.cleaned_data['facture']

            service_date = date_time.isoformat(sep=' ')

            result = gen_calendar(service_id.id_se_dict, service_date, service_date)

            if result is not None:
                result = result[0]
                client = Client.objects.get(client_user_login = request.user.id)

                new_service = Service()
                new_service.service_code = service_id
                new_service.client = client
                new_service.create_invoice = facture
                new_service.planned_start = date_time
                if service_id.avg_time is not None:
                    new_service.planned_end = date_time + datetime.timedelta(minutes = service_id.avg_time)
                new_service.save()

                resources_to_reservation = get_resources_to_reservation(result)
                new_resources_usage = ResourcesUsage()
                new_resources_usage.service = new_service
                new_resources_usage.machine = Machine.objects.get(id_machine = resources_to_reservation['free_machine'])
                new_resources_usage.worker = Worker.objects.get(id_worker = resources_to_reservation['free_worker'])
                new_resources_usage.location = Location.objects.get(id_location = resources_to_reservation['free_location'])
                new_resources_usage.start_timestamp = date_time
                if service_id.avg_time is not None:
                    new_resources_usage.finish_timestamp = date_time + datetime.timedelta(minutes = service_id.avg_time)
                new_resources_usage.calendar_date = WorkdayCalendar(id_workday_calendar = date_time)
                new_resources_usage.save()


                context = {'date' : service_date,
                            'result' : result,
                            'facture' : new_resources_usage.machine}
                return HttpResponse('success')


def reservation(request):

    services_groups = SeGroupDict.objects.all()
    services = SeDict.objects.all()


    context = {'services_groups' : services_groups,
                'services' : services}

    return render(request, 'services/calendar_test.html', context)

def calculate_date_to_display():

    workday_calendar_params = WorkdayCalendarParams.objects.get( id_workday_calendar_params = 1 )
    days_to_display = workday_calendar_params.days_to_display

    start = datetime.datetime.now()
    finish = datetime.date.today() + datetime.timedelta(days = days_to_display)

    return start, finish

def generate_calendar(request):

    if request.method == 'POST' and request.is_ajax():

        service = SeDict.objects.get(id_se_dict = request.POST.get('service_code'))

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

        start, finish = calculate_date_to_display()

        result = gen_calendar(service.id_se_dict, start, finish)

        context = {'result' : result,
                    'service' : service,
                    'workday_start' : workday_start,
                    'workday_end' : workday_end,
                    'display_start' : start,
                    'display_end' : finish
                    }
        # listResult = gen_calendar()
        # result = json.dumps(listResult)
        # result = '/n'.join(record in listResults)
        return render(request, 'services/calendar.html', context)
#    return HttpResonse(result, content_type = "application/json")

# def add(request):
#     sqlResult = sqlSelect()
#     return render(request, 'company/sql.html', {'queryResult': sqlResult})
