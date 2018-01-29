# -*- coding: utf-8 -*-
from django.db import models
from wagtail.wagtailcore.blocks import StructBlock, ListBlock, TextBlock, ChoiceBlock, RichTextBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import StreamField, RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from .constanten import GALLERY

class ImageCarouselBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'image'

class NewsPage(Page):
    intro = RichTextField(default='', blank=True)
    gallery = StreamField([
        ('image', ListBlock(ImageCarouselBlock(), icon="image")),
    ], blank=True)
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('media', ChoiceBlock(choices=GALLERY
            , icon='media'))
    ], null=True, blank=True)
    date_published = models.DateField(
        "Date article published", blank=True, null=True
    )
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        FieldPanel('date_published'),
        StreamFieldPanel('gallery'),
        ImageChooserPanel('feed_image'),
    ]

    parent_page_types = ['NewsIndexPage']

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []

class NewsIndexPage(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
    ]

    # Speficies that only NewsPage objects can live under this index page
    subpage_types = ['NewsPage']

    # Defines a method to access the children of the page (e.g. NewsPage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        context['posts'] = NewsPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context


    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)
