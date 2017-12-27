from django.conf.urls import url
from . import views
from clients.views import clientCRUDlist

app_name = 'workers'
urlpatterns = [
    url(r'^$', views.employee_main, name='employee_index'),
    url(r'^woNotifications/', views.woNotifications, name='woNotifications'),
    url(r'^woNotification/(?P<woNotification_id>\w+)/', views.woNotification, name='woNotification'),
    url(r'^new_woNotification/', views.new_woNotification, name='new_woNotification'),
    url(r'^personal/', views.change_personal_informations, name='personal_informations'),
    url(r'^clients/', clientCRUDlist, name='client_list')

]
