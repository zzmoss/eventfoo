from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$','badge.views.get_details'),

    )
