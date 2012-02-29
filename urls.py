from django.conf.urls.defaults import *
from django.contrib import admin
import django_cron

handler500 = 'djangotoolbox.errorviews.server_error'

admin.autodiscover()
django_cron.autodiscover()

urlpatterns = patterns('',
    url('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('statusapp.urls')),
)
