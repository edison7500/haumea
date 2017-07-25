from django.conf.urls import url
from scrapy.views.web import GoodsListView


urlpatterns = [
    url(r'^$', GoodsListView.as_view(), name='goods-list-view'),
]