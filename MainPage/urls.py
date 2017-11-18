from django.conf.urls import url
from . import views

app_name = 'MainPage'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^about/', views.about, name='about')
    ]
