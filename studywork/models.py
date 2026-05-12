from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable, TranslatableMixin
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images import get_image_model_string

from wagtail_localize.fields import TranslatableField, SynchronizedField


class StudyWorkProgramCard(TranslatableMixin, Orderable):
    page = ParentalKey(
        "studywork.StudyWorkPage",
        on_delete=models.CASCADE,
        related_name="program_cards",
    )

    title = models.CharField(max_length=255)

    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    body_text = models.TextField(
        blank=True,
        help_text="Use plain text. Line breaks and bullet characters will be preserved on the page. This field is easier to translate as one block.",
    )

    button_text = models.CharField(
        max_length=100,
        blank=True,
        default="Contact us about this program",
    )

    translatable_fields = [
        TranslatableField("title"),
        SynchronizedField("image"),
        TranslatableField("body_text"),
        TranslatableField("button_text"),
        SynchronizedField("sort_order"),
    ]

    panels = [
        FieldPanel("title"),
        FieldPanel("image"),
        FieldPanel("body_text"),
        FieldPanel("button_text"),
    ]


class StudyWorkPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        InlinePanel("program_cards", label="Program cards"),
    ]

    parent_page_types = ["home.HomePage"]
    subpage_types = []