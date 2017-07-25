from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from store.views.api import ShopListView, ShopDetailView, EntryListView, EntryDetailView

from django.conf import settings


urlpatterns = [
    url(r'^store/?$', ShopListView.as_view(), name='shop-list-create'),
    url(r'^store/(?P<pk>\d+)/?$', ShopDetailView.as_view(), name='shop-detail'),

    url(r'entry/?$', EntryListView.as_view(), name='entry-list-create'),
    url(r'entry/(?P<pk>\d+)/?$', EntryDetailView.as_view(), name='entry-detail'),

]

if settings.DEBUG == True:
    urlpatterns = format_suffix_patterns(urlpatterns)
else:
    urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', ])