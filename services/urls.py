from django.conf.urls import url
from . import views

app_name = 'services'
urlpatterns = [
    url(r'^$', views.services, name='services'),
    url(r'^reservation/', views.reservation, name='reservation'),
    url(r'^get_calendar/', views.generate_calendar, name='get_calendar'),
    url(r'^summary/', views.generate_summary, name = 'summary'),
    url(r'^save_reservation/', views.save_reservation, name = 'save_reservation'),
]
