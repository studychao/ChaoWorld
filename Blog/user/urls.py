from django.conf.urls import url
from . import views

app_name = 'user'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^dashboard/',views.dashboard,name='dashboard'),
    url(r'^infochange/',views.infochange,name='infochange'),
]