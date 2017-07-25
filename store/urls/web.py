from django.conf.urls import url
from store.views.web import StoreListView, StoreDetailView, EntryView


urlpatterns = [
    url(r'^$', StoreListView.as_view(), name='store-list-view'),
    url(r'^(?P<pk>\d+)/?$', StoreDetailView.as_view(), name='store-detail-view'),
    url(r'^entry/(?P<pk>\d+)/?$', EntryView.as_view(), name='entry-detail-view'),
]