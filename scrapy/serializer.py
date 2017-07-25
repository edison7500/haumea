from rest_framework_mongoengine.serializers import DocumentSerializer
from scrapy.models import Tmall


class TmallSerializer(DocumentSerializer):
    class Meta:
        model = Tmall
        fields = '__all__'
