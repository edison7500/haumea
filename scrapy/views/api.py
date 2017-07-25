from rest_framework_mongoengine.generics import ListAPIView
from rest_framework.filters import OrderingFilter, DjangoFilterBackend
# from django_filters.rest_framework import

from scrapy.serializer import TmallSerializer
from scrapy.models import Tmall


class TmallAPIListView(ListAPIView):
    queryset = Tmall.objects.order_by('-scrapy_mongodb')
    serializer_class = TmallSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('scrapy_mongodb', )
    # filter_fields = ('store_id', )
    # filter_

