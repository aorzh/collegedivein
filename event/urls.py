from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from event.views import EventListView, EventTypeListView, EventDetailView, EventCreateView, EventUpdateView, EventComingListView, EventPopularListView, EventArchiveListView

urlpatterns = patterns('',
    # url(r'^$', 'cdi.views.home', name='home'),
    url(r'^$', EventListView.as_view(), name='event_all'),
    url(r'^coming/$', EventComingListView.as_view(), name='event_coming'),
    url(r'^popular/$', EventPopularListView.as_view(), name='event_popular'),
    url(r'^archive/(?P<year>\d+)/$', EventArchiveListView.as_view(), name='event_archive'),
    url(r'^create/$', login_required(EventCreateView.as_view()), name='event_create'),
    url(r'^type/(?P<slug>\w+)/$', EventTypeListView.as_view(), name='event_type'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),
    url(r'^(?P<slug>\w+)/edit/$', EventUpdateView.as_view(), name='event_update'),
    )
