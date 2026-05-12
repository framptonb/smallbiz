from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.images import get_image_model_string
import feedparser
from django.core.cache import cache


class HomePage(Page):
    hero_logo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_eyebrow = models.CharField(max_length=120, blank=True)
    hero_heading = models.CharField(max_length=255, blank=True)
    hero_text = models.TextField(blank=True)

    primary_button_text = models.CharField(max_length=80, blank=True)
    primary_button_url = models.CharField(max_length=255, blank=True)

    secondary_button_text = models.CharField(max_length=80, blank=True)
    secondary_button_url = models.CharField(max_length=255, blank=True)
    hero_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hero_image_alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Describe the image for accessibility and SEO.",
    )

    show_rss_feed = models.BooleanField(default=True)
    rss_heading = models.CharField(max_length=120, blank=True, default="Immigration headlines")
    rss_feed_url = models.URLField(blank=True)
    rss_item_count = models.PositiveSmallIntegerField(default=3)

    content_panels = Page.content_panels + [
        FieldPanel("hero_image"),
        FieldPanel("hero_logo"),
        FieldPanel("hero_eyebrow"),
        FieldPanel("hero_heading"),
        FieldPanel("hero_text"),
        FieldPanel("primary_button_text"),
        FieldPanel("primary_button_url"),
        FieldPanel("secondary_button_text"),
        FieldPanel("secondary_button_url"),
        FieldPanel("hero_image_alt"),
        FieldPanel("show_rss_feed"),
        FieldPanel("rss_heading"),
        FieldPanel("rss_feed_url"),
        FieldPanel("rss_item_count"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        rss_items = []

        if self.show_rss_feed and self.rss_feed_url:
            cache_key = f"home_rss_feed_{self.id}"
            rss_items = cache.get(cache_key)

            if rss_items is None:
                feed = feedparser.parse(self.rss_feed_url)

                rss_items = []
                for entry in feed.entries[: self.rss_item_count]:
                    rss_items.append({
                        "title": entry.get("title", ""),
                        "link": entry.get("link", ""),
                    })

                cache.set(cache_key, rss_items, 60 * 60)  # cache for 1 hour

        context["rss_items"] = rss_items
        return context