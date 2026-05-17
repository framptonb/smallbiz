from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string


class AboutPage(Page):
    intro = RichTextField(blank=True)
    eyebrow = models.CharField(
        max_length=100,
        blank=True,
        default="About",
    )
    body = RichTextField(blank=True)
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

    certificate_1 = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    certificate_2 = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    certificate_3 = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    certificate_4 = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    certificate_5 = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    about_video_poster = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Poster image shown before the About page video plays.",
    )

    about_video_file = models.FileField(
        upload_to="about/videos/",
        blank=True,
        help_text="Upload an MP4 video file for the About page.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("eyebrow"),
        FieldPanel("body"),
        FieldPanel("hero_image"),
        FieldPanel("hero_image_alt"),
        FieldPanel("certificate_1"),
        FieldPanel("certificate_2"),
        FieldPanel("certificate_3"),
        FieldPanel("certificate_4"),
        FieldPanel("certificate_5"),
        FieldPanel("about_video_poster"),
        FieldPanel("about_video_file"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []

# Create your models here.
