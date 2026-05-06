import re

from django import forms

from .models import CallbackRequest, ContactMessage


class CallbackRequestForm(forms.ModelForm):
    """Форма для заявки на зворотний дзвінок."""

    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"autocomplete": "off", "tabindex": "-1"}),
    )

    class Meta:
        model = CallbackRequest
        fields = ["name", "phone", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Ваше ім'я", "autocomplete": "name"}
            ),
            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+380 XX XXX XX XX",
                    "type": "tel",
                    "autocomplete": "tel",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Додаткові побажання (необов'язково)",
                    "rows": 3,
                }
            ),
        }
        labels = {
            "name": "Ім'я",
            "phone": "Телефон",
            "message": "Повідомлення",
        }

    def clean_website(self) -> str:
        """Honeypot — must be empty."""
        value: str = self.cleaned_data.get("website", "")
        if value:
            raise forms.ValidationError("Недійсна форма.")
        return value

    def clean_phone(self) -> str:
        phone: str = self.cleaned_data.get("phone", "").strip()
        digits = re.sub(r"\D", "", phone)
        if len(digits) < 9:
            raise forms.ValidationError("Введіть коректний номер телефону.")
        return phone


class ContactMessageForm(forms.ModelForm):
    """Форма для повідомлення клієнта (написати)."""

    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"autocomplete": "off", "tabindex": "-1"}),
    )

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Ваше ім'я", "autocomplete": "name"}
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "email@example.com",
                    "autocomplete": "email",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "placeholder": "Ваше повідомлення...",
                    "rows": 4,
                }
            ),
        }
        labels = {
            "name": "Ім'я",
            "email": "E-mail",
            "message": "Повідомлення",
        }

    def clean_website(self) -> str:
        value: str = self.cleaned_data.get("website", "")
        if value:
            raise forms.ValidationError("Недійсна форма.")
        return value
