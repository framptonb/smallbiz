from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable, TranslatableMixin
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.images import get_image_model_string

from wagtail_localize.fields import TranslatableField, SynchronizedField


class WhyUsReason(TranslatableMixin, Orderable):
    page = ParentalKey(
        "whyus.WhyUsPage",
        on_delete=models.CASCADE,
        related_name="reasons",
    )

    subtitle = models.CharField(max_length=255)

    details_text = models.TextField(
        blank=True,
        help_text=(
            "Use plain text. For paragraph breaks, use [[p]]. "
            "For simple line breaks, use [[br]]."
        ),
    )

    bullet_items = models.TextField(
        blank=True,
        help_text=(
            "Enter one bullet item per line. "
            "For Wagtail Localize, you may also use [[br]] between bullet items."
        ),
    )

    open_by_default = models.BooleanField(
        default=False,
        help_text="If selected, this section will be expanded when the page first loads.",
    )

    translatable_fields = [
        TranslatableField("subtitle"),
        TranslatableField("details_text"),
        TranslatableField("bullet_items"),
        SynchronizedField("open_by_default"),
        SynchronizedField("sort_order"),
    ]

    panels = [
        FieldPanel("subtitle"),
        FieldPanel("details_text"),
        FieldPanel("bullet_items"),
        FieldPanel("open_by_default"),
    ]

    class Meta:
        ordering = ["sort_order"]
        constraints = [
            models.UniqueConstraint(
                fields=["translation_key", "locale"],
                name="unique_translation_key_locale_whyus_whyusreason",
            )
        ]


class WhyUsPage(Page):
    eyebrow = models.CharField(
        max_length=100,
        blank=True,
        default="Why Us",
    )

    intro = RichTextField(blank=True)

    main_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    main_image_alt = models.CharField(
        max_length=255,
        blank=True,
        help_text="Describe the image for accessibility and SEO.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("eyebrow"),
        FieldPanel("intro"),
        FieldPanel("main_image"),
        FieldPanel("main_image_alt"),
        InlinePanel("reasons", label="Expandable Why Us sections"),
    ]

    def get_ordered_reasons(self):
        return self.reasons.all().order_by("sort_order", "id")

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    
# Create your models here.
