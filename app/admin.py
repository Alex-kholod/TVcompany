from django.contrib import admin
from .models import *


class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date', 'tv', 'supplier', 'staff', 'count')
    list_filter = ('staff', 'date')
    search_fields = ('tv__tv_model', 'count')
    readonly_fields = ('date',)


admin.site.register(Manufacturer)
admin.site.register(Distributor)
admin.site.register(Car)
admin.site.register(TV)
admin.site.register(Supplier)
admin.site.register(StaffStorage)
admin.site.register(StaffConstructor)
admin.site.register(Storehouse)
admin.site.register(Stocks)
admin.site.register(Shipment)
admin.site.register(Supply, SupplyAdmin)
admin.site.register(BuildLine)
admin.site.register(Build)
admin.site.register(Specifications)
admin.site.register(Matrix)
admin.site.register(Mainplata)
admin.site.register(MatrixType)
admin.site.register(CaseBox)
admin.site.register(Powerboard)
admin.site.register(Loudspeakers)

admin.site.site_title = 'TV Company'
admin.site.site_header = 'Управление Телевизорами'
