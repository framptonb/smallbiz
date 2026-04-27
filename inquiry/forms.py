from django import forms
from django.core.validators import RegexValidator
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


phone_validator = RegexValidator(
    regex=r"^[0-9()+\-\.\s]{7,20}$",
    message="Enter a valid phone number.",
)


class InquiryForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        required=True,
        label="Full name",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your full name",
                "autocomplete": "name",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        label="Email address",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "you@example.com",
                "autocomplete": "email",
            }
        ),
    )

    phone = forms.CharField(
        max_length=20,
        required=True,
        label="Phone number",
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "tel",
                "placeholder": "555-555-5555",
                "autocomplete": "tel",
            }
        ),
    )

    message = forms.CharField(
        required=True,
        label="How can we help?",
        widget=forms.Textarea(
            attrs={
                "class": "form-control form-textarea",
                "rows": 6,
                "placeholder": "Tell us how we can help.",
            }
        ),
    )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean_phone(self):
        return self.cleaned_data["phone"].strip()