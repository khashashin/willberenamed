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
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    parent_page_types = [
        'home.HomePage'
    ]

    content_panels = [
        FieldPanel('title'),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        StreamFieldPanel('gallery'),
        ImageChooserPanel('feed_image'),
    ]
