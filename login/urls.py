from django.conf.urls.defaults import *

urlpatterns = patterns('login.views',
    (r'^$','index'),
    (r'^logout','logout_view'),
    (r'^register','register'),


    )
