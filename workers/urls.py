from django.conf.urls import url
from . import views
from clients.views import clientCRUDlist

app_name = 'workers'
urlpatterns = [
    url(r'^$', views.employee_main, name='employee_index'),
    url(r'^personal/', views.change_personal_informations, name='personal_informations'),
    url(r'^clients/', clientCRUDlist, name='client_list')

]
