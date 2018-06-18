
from django.conf.urls import url

from . import views

app_name = 'board'
urlpatterns = [
               url(r'^comment/board', views.user_comment, name='user_comment'),
               ]
