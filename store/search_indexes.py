from haystack import indexes
from store.models import Shop, Entry


class ShopIndexes(indexes.Indexable, indexes.SearchIndex):

    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', boost=1.25)

    def get_model(self):
        return Shop

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


class EntryIndexes(indexes.Indexable, indexes.SearchIndex):

    text = indexes.CharField(document=True, use_template=True)

    title = indexes.CharField(model_attr='name', boost=1.25)
    shop = indexes.CharField(model_attr='shop', faceted=True, )

    month_average_price = indexes.FloatField(model_attr='month_average_price', stored=True, default=0)

    sales_volume_month = indexes.IntegerField(model_attr='sales_volume_month', stored=True, default=0)

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        return self.get_model().objects.all()


