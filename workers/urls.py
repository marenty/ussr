from django.conf.urls import url
from . import views

app_name = 'workers'
urlpatterns = [
    url(r'^$', views.employee_main, name='employee_main'),
    url(r'^login/', views.employee_login, name='employee_login')
]
