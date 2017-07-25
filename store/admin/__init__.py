from django.contrib import admin
from store.admin.store import ShopAdmin, EntryAdmin, EntryStatAdmin
from store.models import Shop, Entry, EntryStat


admin.site.register(Shop, ShopAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(EntryStat, EntryStatAdmin)



