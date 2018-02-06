from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    FieldRowPanel
)
from wagtail.wagtailcore.fields import StreamField
from colorfield.fields import ColorField
from django.utils.text import slugify


from team_rooster.models import TeamRooster

class MatchPage(Page):
    number = models.PositiveSmallIntegerField(
        unique=True,  # must be unique for use in slug
        help_text="Add the unique number of this Match.")
    starts_at = models.DateTimeField()
    # Team 1
    team_1 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_1_color = ColorField(default='#ff0000', blank=True)
    team_1_score = models.PositiveSmallIntegerField(blank=True)
    # Team 2
    team_2 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_2_color = ColorField(default='#0066ff', blank=True)
    team_2_score = models.PositiveSmallIntegerField(blank=True)


    parent_page_types = ['Matches']
    subpage_types = []

    content_panels = [
        FieldPanel('number', classname="6"),
        FieldPanel('starts_at', classname="6"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_1', classname="12"),
                FieldPanel('team_1_color', classname="6"),
                FieldPanel('team_1_score', classname="6"),
            ]),
        ], heading="Team 1"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_2', classname="12"),
                FieldPanel('team_2_color', classname="6"),
                FieldPanel('team_2_score', classname="6"),
            ]),
        ], heading="Team 2"),
    ]

    def clean(self):
        """Override the values of title and slug before saving."""
        super().clean()
        new_title = 'Match %s' % self.number
        self.title = new_title
        self.slug = slugify(new_title)  # slug MUST be unique & slug-formatted


    class Meta:
        verbose_name_plural = 'matches'

    def __str__(self):
        return '{} vs. {}'.format(self.team_1, self.team_2)

# set a default blank slug for when the editing form renders
# we set this after the model is declared
MatchPage._meta.get_field('slug').default = 'default-blank-slug'

class Matches(Page):
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
    ]

    # Can only have Match children
    subpage_types = ['MatchPage']

    # Returns a queryset of Match objects that are live, that are direct
    # descendants of this index page with most recent first
    def get_matches(self):
        return MatchPage.objects.live().descendant_of(
            self).order_by('-first_published_at')

    # Allows child objects (e.g. Match objects) to be accessible via the
    # template. We use this on the HomePage to display child items of featured
    # content
    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super(Matches, self).get_context(request)
        context['teams'] = MatchPage.objects.descendant_of(
            self).live().order_by(
            '-date_published')
        return context
