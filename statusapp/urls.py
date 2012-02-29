from django.conf.urls.defaults import *
from django.views.generic import ListView
from statusapp.models import Status

urlpatterns = patterns('statusapp.views',
    url('^$',
        ListView.as_view(
            queryset=Status.objects.all(),
            context_object_name='statuses',
            template_name='index.html')),
    url('^update/$', 'update')
)
