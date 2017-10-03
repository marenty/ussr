from django.conf.urls import url
from . import views

app_name = 'clients'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^(?P<blockedReason>[a-zA-Z]+)/$', views.detail, name='blockedReason'),
    
]