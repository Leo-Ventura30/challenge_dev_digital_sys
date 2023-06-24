from django.contrib import admin

from .models import Customers

admin.site.site_header = 'Digital Sys Contract Management'


class CustomersAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'cpf_cnpj', 'score',
                    'value', 'approved_value', 'status', 'updated_at']
    fieldsets = (
        ('Informações do cliente', {
            'fields': (('full_name', 'cpf_cnpj'), 'address')
        }),
        ('Dados do empréstimo', {
            'fields': (('value', 'approved_value'), ('score', 'status'))
        }),
        (None, {
            'fields': (('updated_at', 'created_at'),)
        }),
    )
    readonly_fields = ['score', 'approved_value',
                       'status', 'updated_at', 'created_at']


admin.site.register(Customers, CustomersAdmin)
