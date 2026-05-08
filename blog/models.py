from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images import get_image_model_string


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    hero_eyebrow = models.CharField(max_length=100, blank=True, default="Blog")
    posts_heading = models.CharField(max_length=255, blank=True, default="Latest Posts")
    posts_intro = models.CharField(
        max_length=255,
        blank=True,
        default="Read helpful updates, guidance, and information.",
    )
    article_label = models.CharField(max_length=100, blank=True, default="Article")
    post_card_text = models.CharField(
        max_length=255,
        blank=True,
        default="Read more about this topic and how it may apply to your situation.",
    )
    read_post_text = models.CharField(max_length=100, blank=True, default="Read post →")
    empty_posts_text = models.CharField(max_length=255, blank=True, default="No blog posts yet.")

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("hero_eyebrow"),
        FieldPanel("posts_heading"),
        FieldPanel("posts_intro"),
        FieldPanel("article_label"),
        FieldPanel("post_card_text"),
        FieldPanel("read_post_text"),
        FieldPanel("empty_posts_text"),
    ]

    subpage_types = ["blog.BlogPage"]

    def get_context(self, request):
        context = super().get_context(request)

        context["blog_posts"] = (
            self.get_children()
            .live()
            .specific()
        )

        return context


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField()
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    article_label = models.CharField(max_length=100, blank=True, default="Article")
    back_to_blog_text = models.CharField(max_length=100, blank=True, default="← Back to Blog")

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        FieldPanel("image"),
        FieldPanel("article_label"),
        FieldPanel("back_to_blog_text"),
    ]

    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []