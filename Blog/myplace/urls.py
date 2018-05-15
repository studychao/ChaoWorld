from django.conf.urls import url

from . import views

app_name = 'myplace'
urlpatterns = [
               url(r'^blog/$', views.blog, name='blog'),
               url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
               url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
               url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
               url(r'^tag/(?P<pk>[0-9]+)/$', views.tag, name='tag'),
               url(r'^search/$', views.search, name='search'),
               url(r'^$',views.index,name='index'),
               url(r'^me/$',views.me,name='me'),
               ]
