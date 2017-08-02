from datetime import datetime, timedelta
from django.core import urlresolvers
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_pandas.managers import DataFrameManager


class Shop(models.Model):
    (tmall, taobao, jd) = range(3)
    SHOP_TYPE_CHOICES = [
        (tmall, _('tmall')),
        (taobao, _('taobao')),
        (jd, _('jd'))
    ]

    # slug = fields.RandomCharField(length=12, include_alpha=False, editable=False, db_index=True)
    name = models.CharField(unique=True, max_length=128, blank=True,)
    brief = models.TextField(blank=True, null=True)
    type = models.SmallIntegerField(_('type'), default=tmall, choices=SHOP_TYPE_CHOICES)
    shop_url = models.CharField(unique=True, max_length=255, blank=True)
    created_datetime = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = '商店'
        verbose_name_plural = '商店'

    def __str__(self):
        return "{}".format(self.name)

    def get_absolute_url(self):
        return urlresolvers.reverse('store-detail-view', args=[self.pk, ])

    @property
    def goods_count(self):
        return self.entry.count()


class Entry(models.Model):
    shop = models.ForeignKey(Shop,
                             related_name='entry',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    brief = models.TextField(default='')
    url = models.URLField(max_length=255, null=True, unique=True)
    datetime_created = models.DateTimeField(default=timezone.now, db_index=True)

    objects = DataFrameManager()

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = "商品"

    def __str__(self):
        return "{}".format(self.name)

    @property
    def image_url(self):
        _image_url = self.images.first()
        return _image_url

    @property
    def latest_price(self):
        _price = 0.
        try:
            _price = self.stat.last().price
        except Exception as e:
            pass
        return _price

    @property
    def latest_sale_num(self):
        _sale_num = 0
        try:
            _sale_num = self.stat.last().sale_num
        except Exception as e:
            pass
        return _sale_num

    @property
    def latest_update_date(self):
        date = datetime.now()
        try:
            date = self.stat.last().date_created
        except Exception as e:
            pass
        return date

    @property
    def month_average_price(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        qs = self.stat.filter(date_created__range=(start_date, end_date))
        df = qs.to_dataframe(index='date_created')
        return round(df.price.mean(), 2)

    @property
    def month_average_sale_revenue(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        qs = self.stat.filter(date_created__range=(start_date, end_date))
        df = qs.to_dataframe(index='date_created')
        price_se = df.price.convert_objects(convert_numeric=True)
        sale_se = df.sale_num.diff().fillna(0)
        return round(price_se.mul(sale_se).mean(), 2)

    @property
    def sales_volume_month(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        qs = self.stat.filter(date_created__range=(start_date, end_date))
        df = qs.to_dataframe(index='date_created')
        return df.sale_num.diff().fillna(0).sum()

    @property
    def sales_revenue_month(self):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        qs = self.stat.filter(date_created__range=(start_date, end_date))
        df = qs.to_dataframe(index='date_created')
        price_se = df.price.convert_objects(convert_numeric=True)
        sale_se = df.sale_num.diff().fillna(0)
        return round(price_se.mul(sale_se).sum(), 2)

    def get_absolute_url(self):
        return urlresolvers.reverse('entry-detail-view', args=[self.pk, ])


class EntryStat(models.Model):
    entry = models.ForeignKey(Entry, related_name='stat')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    sale_num = models.IntegerField(default=0)
    date_created = models.DateField(default=timezone.now, db_index=True)

    objects = DataFrameManager()

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '{price} - {sale_num} - {date}'.format(
            price=self.price,
            sale_num=self.sale_num,
            date=self.date_created
        )


class EntryImage(models.Model):
    entry = models.ForeignKey(Entry,
                              related_name='images',
                              on_delete=models.CASCADE)
    image = models.URLField(max_length=255, editable=False)

    def __str__(self):
        return self.image
