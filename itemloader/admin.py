from django.contrib import admin

from .models import Item

# Adds a section where the items can be managed, according
# to the custom definitions
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title','amount','id_num']

admin.site.register(Item, ItemAdmin)
