from django.conf.urls.defaults import *

urlpatterns = patterns('badge.views',
    (r'^$','get_details'), 
#    (r'^/download','get_details("download")'),
#    (r'^/generate','get_details("generate")'),
    )
