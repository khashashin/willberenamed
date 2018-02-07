from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import CharBlock, ChoiceBlock, IntegerBlock, ListBlock
from colorfield.fields import ColorField
from wagtail.wagtailsnippets.models import register_snippet

from team_rooster.models import TeamRooster

class GoupstageTournamentRelationship(Orderable, models.Model):
    page = ParentalKey('TournamentPage', related_name='groupstage_relationship')
    number = models.PositiveSmallIntegerField(required=True,
        help_text="Add the unique number of this Match.")
    starts_at = models.DateTimeField()
    # Team 1
    team_1 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_1_dress = ColorField(default='#ff0000', blank=True)
    team_1_first_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_1_second_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_1_shootout_score = models.PositiveSmallIntegerField(blank=True)
    # Team 2
    team_2 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_2_dress = ColorField(default='#0066ff', blank=True)
    team_2_first_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_2_second_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_2_shootout_score = models.PositiveSmallIntegerField(blank=True)

    panels = [
        FieldPanel('number', classname="6"),
        FieldPanel('starts_at', classname="6"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_1', classname="6"),
                FieldPanel('team_1_color', classname="3"),
                FieldPanel('team_1_score', classname="3"),
            ]),
        ], heading="Team 1"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_2', classname="6"),
                FieldPanel('team_2_color', classname="3"),
                FieldPanel('team_2_score', classname="3"),
            ]),
        ], heading="Team 2"),
    ]

    def __str__(self):
        return '{} vs {} {} - {}'.format(self.team_1, self.team_2, self.starts_at, self.number)

    class Meta:
        verbose_name = 'Gruppenphase Spiel'
        verbose_name_plural = 'Gruppenphase'

class FinalphaseTournamentRelationship(Orderable, models.Model):
    page = ParentalKey('TournamentPage', related_name='final_phase_relationship')
    number = models.PositiveSmallIntegerField(required=True,
        help_text="Add the unique number of this Match.")
    starts_at = models.DateTimeField()
    # Team 1
    team_1 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_1_dress = ColorField(default='#ff0000', blank=True)
    team_1_first_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_1_second_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_1_shootout_score = models.PositiveSmallIntegerField(blank=True)
    # Team 2
    team_2 = models.ForeignKey(
        TeamRooster,
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_2_dress = ColorField(default='#0066ff', blank=True)
    team_2_first_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_2_second_halftime_score = models.PositiveSmallIntegerField(blank=True)
    team_2_shootout_score = models.PositiveSmallIntegerField(blank=True)

    panels = [
        FieldPanel('number', classname="6"),
        FieldPanel('starts_at', classname="6"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_1', classname="6"),
                FieldPanel('team_1_color', classname="3"),
                FieldPanel('team_1_score', classname="3"),
            ]),
        ], heading="Team 1"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('team_2', classname="6"),
                FieldPanel('team_2_color', classname="3"),
                FieldPanel('team_2_score', classname="3"),
            ]),
        ], heading="Team 2"),
    ]

    def __str__(self):
        return '{} vs {} {} - {}'.format(self.team_1, self.team_2, self.starts_at, self.number)

    class Meta:
        verbose_name = 'Finalphase Spiel'
        verbose_name_plural = 'Finalphase'

class TournamentPage(Page):
    starts_at = models.DateTimeField(blank=True)
    ends_at = models.DateTimeField(blank=True)
    # gruppen_phase = StreamField([
    #     ('gruppen_phase', ListBlock(GoupStageMatchStrucktBlock(), icon="plus-inverse")),
    # ], blank=True)
    # final_phase = StreamField([
    #     ('final_phase', ListBlock(FinalStageMatchStrucktBlock(), icon="pick")),
    # ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('starts_at'),
        FieldPanel('ends_at'),
        InlinePanel(
            'groupstage_relationship', label="Goups",
            panels=None, min_num=1),
        InlinePanel(
            'final_phase_relationship', label="Finals",
            panels=None, min_num=1),
    ]

    def __str__(self):
        return self.title

class ScreencastPage(Page):
    # playing_first = models.ForeignKey(
    #     TournamentPage.gruppen_phase.# One of the GoupStageMatchStrucktBlock() from TournamentPage
    # )
    # playing_next = models.ForeignKey(
    #     TournamentPage.gruppen_phase.# Another one of the GoupStageMatchStrucktBlock() from TournamentPage
    # )

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        InlinePanel(
            'groupstage_relationship', label="Playing First",
            panels=None, max_num=1),
        InlinePanel(
            'final_phase_relationship', label="Playing Next",
            panels=None, max_num=1),
    ]

    subpage_types = []

    def __str__(self):
        return self.title
