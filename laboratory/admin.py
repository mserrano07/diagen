from django.contrib import admin
from .models import Reagent, Consumables, Provider, Location, KitInformation, LoteKit

admin.site.site_header = 'Diagen Admin'
admin.site.register([Location, ])


class ConsumablesAdmin(admin.ModelAdmin):

    list_display = ['name', 'size', 'location', 'stock', 'batch_code', 'provider']
    search_fields = ['name', 'location', 'batch_code', 'provider__name']


class KitInformationAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'sumary', 'public', 'status']
    search_fields = ['name', 'sumary']


class ProviderAdmin(admin.ModelAdmin):

    list_display = ['name']
    search_fields = ['name']


class ReagentAdmin(admin.ModelAdmin):

    list_display = ['name', 'exp_date', 'size', 'weight', 'location', 'type_ac', 'stock', 'batch_code', 'provider']
    search_fields = ['name', 'size', 'weight', 'location', 'batch_code', 'provider']


class LoteKitAdmin(admin.ModelAdmin):

    list_display = ['code', 'stock', 'exp_date']
    search_fields = ['code']


admin.site.register(Consumables, ConsumablesAdmin)

admin.site.register(Reagent, ReagentAdmin)

admin.site.register(LoteKit, LoteKitAdmin)

admin.site.register(Provider, ProviderAdmin)

admin.site.register(KitInformation, KitInformationAdmin)
