from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','login.views.index'),

    (r'^register','login.views.register'),


    )
