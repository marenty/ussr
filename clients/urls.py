from django.conf.urls import url
from . import views

app_name = 'clients'
urlpatterns = [
    url(r'^personal/', views.change_personal_informations, name='personal_informations'),
    url(r'^create_client/', views.CreateClient, name='create_client'),
    url(r'^delete_clients/', views.DeleteClient, name='delete_clients'),
    url(r'^edit_client_form/', views.EditClientFormFill, name='edit_client_form_fill'),
    url(r'^edit_client/', views.EditClient, name='edit_client'),
]
