from django.core.mail import send_mail

def EmailCheck(client):

    if (client.address is None):
        return False
    elif (client.address.email is None):
        return False
    else:
        return True

def SendReservationConfirmEmail(client, service_dict, resource_usage):
    send_mail(
    "Potwierdzenie rezerwacji usługi",
    'Potwierdzenie rezerwacji usługi\n'+
    'Zarezerwowałeś usługę ' + service_dict.se_dict_name +
    '\nPlanowany termin: ' + resource_usage.start_timestamp.strftime("%Y-%m-%d %H:%M") +
    '\nPracownik, który planowo świadczył będzie usługę to ' + resource_usage.worker.get_employee_name() +
    ".\nW razie pytań prosimy o kontakt\n",
    "Pomorończe",
    [client.address.email],
    fail_silently=False)
