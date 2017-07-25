import pygal
from django.views.generic import ListView, DetailView
from django.utils.log import getLogger
from pygal import Config

from store.models import Shop, Entry
from datetime import datetime, timedelta


logger = getLogger('django')


class StoreListView(ListView):
    model = Shop
    queryset = Shop.objects.all()
    template_name = 'store/list.html'
    paginate_by = 20


class StoreDetailView(ListView):
    model = Entry
    template_name = 'store/detail.html'
    paginate_by = 20

    def get_queryset(self):
        self.queryset = Entry.objects.filter(shop_id=self.store_id)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store = Shop.objects.get(pk = self.store_id)
        context.update({
            'store': store,
        })
        return context

    def get(self, request, *args, **kwargs):
        self.store_id = kwargs.pop('pk')
        return super().get(request, *args, **kwargs)


class EntryView(DetailView):
    model = Entry
    template_name = 'entry/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        stat = self.object.stat.filter(date_created__range=(start_date, end_date))
        df = stat.to_dataframe(index='date_created')
        context.update({
            'sale_chart': self.get_sale_chart(stat, df=df),
            'price_chart': self.get_price_chart(stat),
        })

        return context

    def get_sale_chart(self, stat, df):
        config = Config()
        config.show_legend = False
        config.human_readable = True
        # config.fill = True
        config.x_label_rotation = 90
        config.pretty_print = True
        config.min_scale = 12
        # config.print_values = True
        # config.print_values_position = 'top'
        # config.value_font_size=30

        sale_chart = pygal.Line(config)
        sale_chart.title = '总销量走势图'
        sale_chart.x_labels =  map(lambda x: x.date_created.strftime("%Y-%m-%d"), stat)
        price_se = df.price.convert_objects(convert_numeric=True)
        sale_se = df.sale_num.diff().fillna(0)
        sale_chart.add('销量', [row for row in sale_se])
        sale_chart.add('销售额', [row for row in price_se.mul(sale_se)], secondary=True)
        return sale_chart.render()

    def get_price_chart(self, stat):
        config = Config()
        config.show_legend = False
        config.human_readable = True
        config.x_label_rotation = 90
        config.pretty_print = True
        config.min_scale = 12

        price_chart = pygal.Line(config)
        price_chart.title = '售价走势图'
        price_chart.x_labels = map(lambda x: x.date_created.strftime("%Y-%m-%d"), stat)
        price_chart.add('价格', [row.price for row in stat])
        return price_chart.render()



