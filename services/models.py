from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string


class ServicesIndexPage(Page):
    intro = RichTextField(blank=True)

    hero_eyebrow = models.CharField(max_length=100, blank=True, default="Services")
    services_heading = models.CharField(max_length=255, blank=True, default="Immigration Services")
    services_intro = models.CharField(
        max_length=255,
        blank=True,
        default="Explore our available service areas and choose the option that best fits your needs.",
    )
    service_card_text = models.CharField(
        max_length=255,
        blank=True,
        default="Learn more about this service and how we can help.",
    )
    view_service_text = models.CharField(max_length=100, blank=True, default="View service →")
    empty_services_text = models.CharField(max_length=255, blank=True, default="No services available yet.")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("hero_eyebrow"),
        FieldPanel("services_heading"),
        FieldPanel("services_intro"),
        FieldPanel("service_card_text"),
        FieldPanel("view_service_text"),
        FieldPanel("empty_services_text"),
    ]

    subpage_types = ["services.ServicePage"]


class ServicePage(Page):
    short_summary = models.CharField(max_length=255)
    body = RichTextField()
    price_note = models.CharField(max_length=120, blank=True)
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    hero_eyebrow = models.CharField(max_length=100, blank=True, default="Service")
    sidebar_heading = models.CharField(max_length=100, blank=True, default="Need help?")
    sidebar_text = models.CharField(
        max_length=255,
        blank=True,
        default="Send us an inquiry and we’ll respond with the next steps.",
    )
    sidebar_button_text = models.CharField(max_length=100, blank=True, default="Send an Inquiry")
    pricing_note_heading = models.CharField(max_length=100, blank=True, default="Pricing note")
    back_to_services_text = models.CharField(max_length=100, blank=True, default="← Back to Services")

    content_panels = Page.content_panels + [
        FieldPanel("short_summary"),
        FieldPanel("body"),
        FieldPanel("price_note"),
        FieldPanel("image"),
        FieldPanel("hero_eyebrow"),
        FieldPanel("sidebar_heading"),
        FieldPanel("sidebar_text"),
        FieldPanel("sidebar_button_text"),
        FieldPanel("pricing_note_heading"),
        FieldPanel("back_to_services_text"),
    ]

    parent_page_types = ["services.ServicesIndexPage"]
    subpage_types = []