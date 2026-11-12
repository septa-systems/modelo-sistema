from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Empresa, Usuario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ["nome", "criada_em"]
    search_fields = ["nome"]


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    list_display = ["username", "email", "empresa", "is_staff", "is_active"]
    list_filter = ["empresa", "is_staff", "is_active"]
    fieldsets = [*UserAdmin.fieldsets, ("Empresa", {"fields": ["empresa"]})]
