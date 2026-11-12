from django import forms

from .services import normalizar_telefone


class ClienteForm(forms.Form):
    nome = forms.CharField(max_length=150)
    telefone = forms.CharField(max_length=20, help_text="Com DDD. Ex.: (11) 98888-7777")
    email = forms.EmailField(required=False, label="E-mail")

    def clean_telefone(self):
        telefone = normalizar_telefone(self.cleaned_data["telefone"])
        if not 10 <= len(telefone) <= 13:
            raise forms.ValidationError("Telefone inválido. Use DDD + número.")
        return telefone
