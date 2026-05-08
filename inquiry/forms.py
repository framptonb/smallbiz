from django import forms
from django.core.validators import RegexValidator


phone_validator = RegexValidator(
    regex=r"^[0-9()+\-\.\s]{7,20}$",
    message="Enter a valid phone number.",
)


class InquiryForm(forms.Form):
    name = forms.CharField(max_length=120, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(
        max_length=20,
        required=True,
        validators=[phone_validator],
    )
    message = forms.CharField(required=True)

    def __init__(self, *args, page=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].label = page.name_label if page else "Full name"
        self.fields["name"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": page.name_placeholder if page else "Your full name",
                "autocomplete": "name",
            }
        )

        self.fields["email"].label = page.email_label if page else "Email address"
        self.fields["email"].widget = forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": page.email_placeholder if page else "you@example.com",
                "autocomplete": "email",
            }
        )

        self.fields["phone"].label = page.phone_label if page else "Phone number"
        self.fields["phone"].widget = forms.TextInput(
            attrs={
                "class": "form-control",
                "type": "tel",
                "placeholder": page.phone_placeholder if page else "555-555-5555",
                "autocomplete": "tel",
            }
        )

        self.fields["message"].label = page.message_label if page else "How can we help?"
        self.fields["message"].widget = forms.Textarea(
            attrs={
                "class": "form-control form-textarea",
                "rows": 6,
                "placeholder": page.message_placeholder if page else "Tell us how we can help.",
            }
        )

    def clean_phone(self):
        return self.cleaned_data["phone"].strip()