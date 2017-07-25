from django.views.generic import ListView
from scrapy.models import Tmall


class GoodsListView(ListView):

    # queryset = Tmall.objects.order_by('-price', )
    queryset = Tmall.objects.order_by('-sale_num')
    model = Tmall
    template_name = 'scrapy/list.html'
    paginate_by = 32