from django.core.mail import send_mail
from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page

from .forms import InquiryForm
from django.shortcuts import render
from django.conf import settings

class InquiryPage(Page):
    template = "inquiry/inquiry_page.html"

    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    hero_eyebrow = models.CharField(max_length=100, blank=True, default="Contact us")
    submit_button_text = models.CharField(max_length=100, blank=True, default="Send Inquiry")

    name_label = models.CharField(max_length=100, blank=True, default="Full name")
    name_placeholder = models.CharField(max_length=100, blank=True, default="Your full name")

    email_label = models.CharField(max_length=100, blank=True, default="Email address")
    email_placeholder = models.CharField(max_length=100, blank=True, default="you@example.com")

    phone_label = models.CharField(max_length=100, blank=True, default="Phone number")
    phone_placeholder = models.CharField(max_length=100, blank=True, default="555-555-5555")

    message_label = models.CharField(max_length=100, blank=True, default="How can we help?")
    message_placeholder = models.CharField(max_length=255, blank=True, default="Tell us how we can help.")

    captcha_label = models.CharField(max_length=100, blank=True, default="Captcha")

    email_to = models.EmailField(
        blank=True,
        help_text="Where inquiry notifications should be sent.",
    )
    email_from = models.EmailField(
        blank=True,
        help_text="Optional from address for notification emails.",
    )
    email_subject = models.CharField(
        max_length=255,
        blank=True,
        default="New website inquiry",
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = []
    max_count = 1

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("thank_you_text"),
        FieldPanel("email_to"),
        FieldPanel("email_from"),
        FieldPanel("email_subject"),
        FieldPanel("hero_eyebrow"),
        FieldPanel("submit_button_text"),
        FieldPanel("name_label"),
        FieldPanel("name_placeholder"),
        FieldPanel("email_label"),
        FieldPanel("email_placeholder"),
        FieldPanel("phone_label"),
        FieldPanel("phone_placeholder"),
        FieldPanel("message_label"),
        FieldPanel("message_placeholder"),
        FieldPanel("captcha_label"),
    ]

    def get_form_class(self):
        return InquiryForm

    def serve(self, request):
        form_class = self.get_form_class()

        if request.method == "POST":
            form = form_class(request.POST, page=self)
            if form.is_valid():
                self.process_form_submission(form)
                return render(
                    request,
                    "inquiry/inquiry_page_landing.html",
                    {
                        "page": self,
                    },
                )
        else:
            form = form_class(page=self)

        return render(
            request,
            "inquiry/inquiry_page.html",
            {
                "page": self,
                "form": form,
            },
        )

    def process_form_submission(self, form):
        cleaned = form.cleaned_data.copy()
       
        if self.email_to:
            message = (
                f"New inquiry received\n\n"
                f"Name: {cleaned['name']}\n"
                f"Email: {cleaned['email']}\n"
                f"Phone: {cleaned['phone']}\n\n"
                f"Message:\n{cleaned['message']}\n"
            )

            send_mail(
                subject=self.email_subject or "New website inquiry",
                message=message,
                from_email=self.email_from or settings.DEFAULT_FROM_EMAIL,
                recipient_list=[self.email_to],
                fail_silently=False,
            )

# Create your models here.
