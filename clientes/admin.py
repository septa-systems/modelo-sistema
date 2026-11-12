from django.contrib import admin

from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome", "empresa", "criado_em"]
    list_filter = ["empresa"]
    search_fields = ["nome"]
