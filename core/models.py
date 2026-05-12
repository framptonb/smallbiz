from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel


@register_setting
class BusinessSettings(BaseSiteSetting):
    business_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    hours = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    wechat_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="WeChat ID or contact handle"
    )

    panels = [
        FieldPanel("business_name"),
        FieldPanel("phone"),
        FieldPanel("email"),
        FieldPanel("address"),
        FieldPanel("hours"),
        FieldPanel("facebook_url"),
        FieldPanel("instagram_url"),
        FieldPanel("wechat_id"),
    ]

# Create your models here.
