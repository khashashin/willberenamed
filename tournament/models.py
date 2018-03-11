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
import json
from django.http import HttpResponse
from django.forms.utils import pretty_name
from django.utils.html import format_html
from wagtail.wagtailadmin.edit_handlers import EditHandler
from django.core.serializers.json import DjangoJSONEncoder

from team_rooster.models import TeamRooster

# Read only panel to use in admin panels
class BaseReadOnlyPanel(EditHandler):
    def render(self):
        value = getattr(self.instance, self.attr)
        if callable(value):
            value = value()
        return format_html('<div style="padding: 1.2em;">{}</div>', value)

    def render_as_object(self):
        return format_html(
            '<fieldset><legend>{}</legend>'
            '<ul class="fields"><li><div class="field"><div class="field-content"><div style="background-color: #eeeeee; border-radius: 5px" class="input">{}</div></div></div></li></ul>'
            '</fieldset>',
            self.heading, self.render())

    def render_as_field(self):
        return format_html(
            '<div class="field">'
            '<label>{}{}</label>'
            '<div class="field-content">{}</div>'
            '</div>',
            self.heading, _(':'), self.render())


class ReadOnlyPanel:
    def __init__(self, attr, heading=None, classname=''):
        self.attr = attr
        self.heading = pretty_name(self.attr) if heading is None else heading
        self.classname = classname

    def bind_to_model(self, model):
        return type(str(_('ReadOnlyPanel')), (BaseReadOnlyPanel,),
                    {'attr': self.attr, 'heading': self.heading,
                     'classname': self.classname})

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
    team_1_first_halftime_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat 1. HZ')
    team_1_first_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 1. HZ')
    team_1_second_halftime_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat 2. HZ')
    team_1_second_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 2. HZ')
    team_1_shootout_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat Shootout')
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
    team_2_first_halftime_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat 1. HZ')
    team_2_first_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 1. HZ')
    team_2_second_halftime_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat 2. HZ')
    team_2_second_halftime_point = models.PositiveSmallIntegerField(blank=True, default=0, verbose_name='Punkte 2. HZ')
    team_2_shootout_score = models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Resultat Shootout')
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
        ReadOnlyPanel('team_1_total_score', classname="col3"),
        ReadOnlyPanel('team_1_first_halftime_point', classname="col3"),
        ReadOnlyPanel('team_1_second_halftime_point', classname="col3"),
        ReadOnlyPanel('team_1_shootout_point', classname="col3"),
        ReadOnlyPanel('team_1_total_points', classname="col3"),
        # Team 2
        FieldPanel('team_2', classname="col9"),
        FieldPanel('team_2_dress', classname="col3"),
        FieldPanel('team_2_first_halftime_score', classname="col3"),
        FieldPanel('team_2_second_halftime_score', classname="col3"),
        FieldPanel('team_2_shootout_score', classname="col3"),
        ReadOnlyPanel('team_2_total_score', classname="col3"),
        ReadOnlyPanel('team_2_first_halftime_point', classname="col3"),
        ReadOnlyPanel('team_2_second_halftime_point', classname="col3"),
        ReadOnlyPanel('team_2_shootout_point', classname="col3"),
        ReadOnlyPanel('team_2_total_points', classname="col3"),
    ]

    @receiver(pre_save, sender='tournament.GroupstageTournamentModel')
    def my_callback(sender, instance, *args, **kwargs):
        # Point for first half time
        if not (instance.team_1_first_halftime_score is None or instance.team_2_first_halftime_score is None):
            if instance.team_1_first_halftime_score > instance.team_2_first_halftime_score:
                instance.team_1_first_halftime_point = 2
            elif instance.team_2_first_halftime_score > instance.team_1_first_halftime_score:
                instance.team_2_first_halftime_point = 2
            elif instance.team_1_first_halftime_score == instance.team_2_first_halftime_score:
                instance.team_2_first_halftime_point = 1
                instance.team_1_first_halftime_point = 1
        # Point for second half time
        if not (instance.team_1_second_halftime_score is None or instance.team_2_second_halftime_score is None):
            if instance.team_1_second_halftime_score > instance.team_2_second_halftime_score:
                instance.team_1_second_halftime_point = 2
            elif instance.team_2_second_halftime_score > instance.team_1_second_halftime_score:
                instance.team_2_second_halftime_point = 2
            elif instance.team_1_second_halftime_score == instance.team_2_second_halftime_score:
                instance.team_2_second_halftime_point = 1
                instance.team_1_second_halftime_point = 1
        # Point for Shootout
        if not (instance.team_1_shootout_score is None or instance.team_2_shootout_score is None):
            if instance.team_1_shootout_score > instance.team_2_shootout_score:
                instance.team_1_shootout_point = 1
            elif instance.team_2_shootout_score > instance.team_1_shootout_score:
                instance.team_2_shootout_point = 1
            elif instance.team_1_shootout_score == instance.team_2_shootout_score:
                instance.team_1_shootout_point = 0
                instance.team_2_shootout_point = 0
        # Total score calculation Team 1
        if not (instance.team_1_first_halftime_score is None):
            if instance.team_1_first_halftime_score >= 0:
                instance.team_1_total_score = instance.team_1_first_halftime_score
                if not (instance.team_1_second_halftime_score is None):
                    if instance.team_1_second_halftime_score >= 0:
                        instance.team_1_total_score = instance.team_1_first_halftime_score + instance.team_1_second_halftime_score
                        if not (instance.team_1_shootout_score is None):
                            if instance.team_1_shootout_score >= 0:
                                instance.team_1_total_score = instance.team_1_first_halftime_score + instance.team_1_second_halftime_score + instance.team_1_shootout_point
        # Total score calculation Team 2
        if not (instance.team_2_first_halftime_score is None):
            if instance.team_2_first_halftime_score >= 0:
                instance.team_2_total_score = instance.team_2_first_halftime_score
                if not (instance.team_2_second_halftime_score is None):
                    if instance.team_2_second_halftime_score >= 0:
                        instance.team_2_total_score = instance.team_2_first_halftime_score + instance.team_2_second_halftime_score
                        if not (instance.team_2_shootout_score is None):
                            if instance.team_2_shootout_score >= 0:
                                instance.team_2_total_score = instance.team_2_first_halftime_score + instance.team_2_second_halftime_score + instance.team_2_shootout_point
        if (instance.team_1_first_halftime_score is None or instance.team_1_second_halftime_score is None or instance.team_1_shootout_score is None):
            if instance.team_1_first_halftime_score is None:
                instance.team_1_first_halftime_point = 0
            if instance.team_1_second_halftime_score is None:
                instance.team_1_second_halftime_point = 0
            if instance.team_1_shootout_score is None:
                instance.team_1_shootout_point = 0
        if (instance.team_2_first_halftime_score is None or instance.team_2_second_halftime_score is None or instance.team_2_shootout_score is None):
            if instance.team_2_first_halftime_score is None:
                instance.team_2_first_halftime_point = 0
            if instance.team_2_second_halftime_score is None:
                instance.team_2_second_halftime_point = 0
            if instance.team_2_shootout_score is None:
                instance.team_2_shootout_point = 0
        if (instance.team_1_first_halftime_score is None and instance.team_1_second_halftime_score is None and instance.team_1_shootout_score is None):
            instance.team_1_total_score = 0
        if (instance.team_2_first_halftime_score is None and instance.team_2_second_halftime_score is None and instance.team_2_shootout_score is None):
            instance.team_2_total_score = 0
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

    def serve(self, request):
        if request.is_ajax():
            result = []
            for match in self.matches():
                team_1_logo = match.team_1.team_logo.get_rendition('width-400')
                team_2_logo = match.team_2.team_logo.get_rendition('width-400')
                beginnt_date = json.dumps(match.starts_at.date().strftime("%d-%m-%Y"), cls=DjangoJSONEncoder)
                beginnt_zeit = json.dumps(match.starts_at.time().strftime("%H:%M"), cls=DjangoJSONEncoder)
                result.append({
                    'beginnt_date': beginnt_date,
                    'beginnt_zeit': beginnt_zeit,
                    'team_1_name': match.team_1.title,
                    'team_1_score': match.team_1_total_score,
                    'team_1_logo': team_1_logo.url,
                    'team_2_name': match.team_2.title,
                    'team_2_score': match.team_2_total_score,
                    'team_2_logo': team_2_logo.url,
                })

            json_output = json.dumps(result)
            return HttpResponse(json_output)
        else:
            return super(ScreencastPage, self).serve(request)
