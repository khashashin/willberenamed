from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
    FieldRowPanel,
    InlinePanel,
    PageChooserPanel
)
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.blocks import CharBlock, ChoiceBlock, IntegerBlock, ListBlock
from colorfield.fields import ColorField
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from team_rooster.models import TeamRooster

@register_snippet
class GroupstageTournamentModel(ClusterableModel):
    number = models.PositiveSmallIntegerField(
        verbose_name="Match №:")
    starts_at = models.DateTimeField()
    # Team 1
    team_1 = models.ForeignKey(
        TeamRooster,
        null=True, verbose_name='Erste Team',
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_1_dress = ColorField(blank=True, verbose_name='Dress')
    team_1_first_halftime_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat 1. HZ')
    team_1_first_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 1. HZ')
    team_1_second_halftime_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat 2. HZ')
    team_1_second_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 2. HZ')
    team_1_shootout_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat Shootout')
    team_1_shootout_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Schootout Punkte')
    team_1_total_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat Total')
    team_1_total_points = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte Total')

    # Team 2
    team_2 = models.ForeignKey(
        TeamRooster,
        null=True, verbose_name='Zweite Team',
        on_delete=models.SET_NULL,
        related_name="+",
    )
    team_2_dress = ColorField(blank=True, verbose_name='Dress')
    team_2_first_halftime_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat 1. HZ')
    team_2_first_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 1. HZ')
    team_2_second_halftime_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat 2. HZ')
    team_2_second_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 2. HZ')
    team_2_shootout_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat Shootout')
    team_2_shootout_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Schootout Punkte')
    team_2_total_score = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Resultat Total')
    team_2_total_points = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte Total')

    panels = [
        FieldPanel('number', classname="col6"),
        FieldPanel('starts_at', classname="col6"),
        # Team 1
        FieldPanel('team_1', classname="col9"),
        FieldPanel('team_1_dress', classname="col3"),
        FieldPanel('team_1_first_halftime_score', classname="col3"),
        FieldPanel('team_1_second_halftime_score', classname="col3"),
        FieldPanel('team_1_shootout_score', classname="col3"),
        FieldPanel('team_1_total_score', classname="col3"),
        FieldPanel('team_1_first_halftime_point', classname="col3"),
        FieldPanel('team_1_second_halftime_point', classname="col3"),
        FieldPanel('team_1_shootout_point', classname="col3"),
        FieldPanel('team_1_total_points', classname="col3"),
        # Team 2
        FieldPanel('team_2', classname="col9"),
        FieldPanel('team_2_dress', classname="col3"),
        FieldPanel('team_2_first_halftime_score', classname="col3"),
        FieldPanel('team_2_second_halftime_score', classname="col3"),
        FieldPanel('team_2_shootout_score', classname="col3"),
        FieldPanel('team_2_total_score', classname="col3"),
        FieldPanel('team_2_first_halftime_point', classname="col3"),
        FieldPanel('team_2_second_halftime_point', classname="col3"),
        FieldPanel('team_2_shootout_point', classname="col3"),
        FieldPanel('team_2_total_points', classname="col3"),
    ]

    @receiver(pre_save, sender='tournament.GroupstageTournamentModel')
    def my_callback(sender, instance, *args, **kwargs):
        instance.team_1_total_score = instance.team_1_first_halftime_score + instance.team_1_second_halftime_score + instance.team_1_shootout_score
        instance.team_2_total_score = instance.team_2_first_halftime_score + instance.team_2_second_halftime_score + instance.team_2_shootout_score
        instance.team_1_total_points = instance.team_1_first_halftime_point + instance.team_1_second_halftime_point + instance.team_1_shootout_point
        instance.team_2_total_points = instance.team_2_first_halftime_point + instance.team_2_second_halftime_point + instance.team_2_shootout_point

    def __str__(self):
        return 'Match №:{} Begint: {} {} vs {}'.format(self.number, self.starts_at, self.team_1, self.team_2)

    class Meta:
        verbose_name = 'Gruppenphase Spiel'
        verbose_name_plural = 'Gruppenphase'

class GroupstageScreencastRelationship(Orderable, models.Model):
    page = ParentalKey('ScreencastPage',
        related_name='groupstage_screencast_relationship')
    match = models.ForeignKey('GroupstageTournamentModel',
        related_name='match_screen_relationship')
    panels = [
        SnippetChooserPanel('match')
    ]


class ScreencastPage(Page):
    content_panels = Page.content_panels + [
        InlinePanel(
            'groupstage_screencast_relationship', label="Choose Teams",
            panels=None, max_num=2),
    ]

    parent_page_types = ['home.HomePage']

    def matches(self):
        matches = [
            n.match for n in self.groupstage_screencast_relationship.all()
        ]

        return matches
