from django.contrib import admin

from api.models import store, storeItem

class StoreAdmin(admin.ModelAdmin):
	pass

class StoreItemAdmin(admin.ModelAdmin):
	pass

admin.site.register(store, StoreAdmin)
admin.site.register(storeItem, StoreItemAdmin)