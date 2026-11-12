from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.urls import include, path
from django.views.generic import RedirectView
from django_otp.admin import OTPAdminSite

# Admin só entra com 2FA (docs/SEGURANCA.md). Crie o código com: manage.py criar_2fa <usuario>
admin.site.__class__ = OTPAdminSite


def saude(request):
    """Usado pelo servidor para saber se o sistema está no ar."""
    return HttpResponse("ok")


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("entrar/", auth_views.LoginView.as_view(), name="login"),
    path("sair/", auth_views.LogoutView.as_view(), name="logout"),
    path("clientes/", include("clientes.urls")),
    path("saude/", saude, name="saude"),
    path("", RedirectView.as_view(pattern_name="clientes:lista", permanent=False)),
]
