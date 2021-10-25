from django.contrib import admin
from .models import ContractForm


class ContractFormAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'tipoNegocio', 'descricao')
    list_display_links = ('id','email', 'tipoNegocio', 'descricao')
    list_filter = ('id','email', 'tipoNegocio', 'descricao')
    list_per_page = 10
    search_fields = ('id','email', 'tipoNegocio', 'descricao')


admin.site.register(ContractForm, ContractFormAdmin)