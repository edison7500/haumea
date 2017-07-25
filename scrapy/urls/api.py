from django.conf.urls import url
from scrapy.views.api import TmallAPIListView


urlpatterns = [
    url(r'^tmall/?$', TmallAPIListView.as_view(), name='api-tmall-list-view'),
]