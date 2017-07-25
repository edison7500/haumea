from django.contrib import admin


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'goods_count', 'shop_url', 'created_datetime', ]
    list_editable = ['type',]
    list_filter = ['type', ]
    search_fields = ['name', ]


class EntryAdmin(admin.ModelAdmin):
    list_display = ['name', 'shop', 'url', 'latest_price', 'datetime_created',]
    search_fields = ['name', ]


class EntryStatAdmin(admin.ModelAdmin):
    list_display = ['entry', 'price', 'sale_num', 'date_created']
    search_fields = ['entry__name', ]
