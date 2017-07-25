from rest_framework import serializers
from store.models import Shop, Entry, EntryStat


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'brief', 'type', 'shop_url', )
        read_only_fields = ('created_datetime', )


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ('id', 'name', 'shop', 'url')


class EntryStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryStat
        fields = ('id', 'price', 'sale_num')