from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    hero_eyebrow = models.CharField(max_length=120, blank=True)
    hero_heading = models.CharField(max_length=255, blank=True)
    hero_text = models.TextField(blank=True)

    primary_button_text = models.CharField(max_length=80, blank=True)
    primary_button_url = models.CharField(max_length=255, blank=True)

    secondary_button_text = models.CharField(max_length=80, blank=True)
    secondary_button_url = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("hero_eyebrow"),
        FieldPanel("hero_heading"),
        FieldPanel("hero_text"),
        FieldPanel("primary_button_text"),
        FieldPanel("primary_button_url"),
        FieldPanel("secondary_button_text"),
        FieldPanel("secondary_button_url"),
    ]