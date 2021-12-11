from django.contrib import admin

from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['ref_id', 'order_number', 'description', 'amount']
    search_fields = ['ref_id', 'order_number']


admin.site.register(Transaction, TransactionAdmin)
