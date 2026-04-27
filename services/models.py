from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string


class ServicesIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
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

    content_panels = Page.content_panels + [
        FieldPanel("short_summary"),
        FieldPanel("body"),
        FieldPanel("price_note"),
        FieldPanel("image"),
    ]

    parent_page_types = ["services.ServicesIndexPage"]
    subpage_types = []
