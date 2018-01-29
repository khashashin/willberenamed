from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.wagtailcore.blocks import StructBlock, CharBlock, ChoiceBlock, IntegerBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailblocks_cards.blocks import CardsBlock
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.wagtailcore.fields import StreamField
from .constanten import POSITIONS, POSITIONS_SP


class Staff(StructBlock):
    photo = ImageChooserBlock(required=False)
    name = CharBlock(required=True)
    vorname = CharBlock(required=True)
    position = ChoiceBlock(choices=POSITIONS, icon='cup')

    class Meta:
        icon = 'plus'

class Spieler(StructBlock):
    photo = ImageChooserBlock(required=False)
    nummer = IntegerBlock(required=True)
    name = CharBlock(required=True)
    vorname = CharBlock(required=True)
    position = ChoiceBlock(choices=POSITIONS_SP, icon='cup')
    jahrgang = IntegerBlock(required=True)

    class Meta:
        icon = 'user'

class TeamRooster(Page):
    team_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    staff = StreamField([
        ('staff', CardsBlock(Staff(), icon="plus")),
    ], blank=True)
    spieler = StreamField([
        ('spieler', CardsBlock(Spieler(), icon="user")),
    ], blank=True)

    parent_page_types = ['Teams']

    content_panels = [
        FieldPanel('title'),
        ImageChooserPanel('team_logo'),
        StreamFieldPanel('staff'),
        StreamFieldPanel('spieler'),
    ]

    def __str__(self):
        return self.team_name


# Create your models here.
class Teams(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

    # Can only have TeamRooster children
    subpage_types = ['TeamRooster']

    # Returns a queryset of TeamRooster objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_teams(self):
        return TeamRooster.objects.live().descendant_of(
            self).order_by('-first_published_at')

    # Allows child objects (e.g. TeamRooster objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super(Teams, self).get_context(request)
        context['teams'] = TeamRooster.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context
