# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster
from news.models import NewsPage
# from matches.models import MatchPage
from tournament.models import (
    GroupstageTournamentModel, ScreencastPage)

class MaxFiveMatchFilter(admin.SimpleListFilter):
    title = _('Match №:')
    parameter_name = 'fivematches'

    def lookups(self, request, model_admin):
        return (
            ('match 1-5', _('match 1-5')),
            ('match 5-10', _('match 5-10')),
            ('match 10-15', _('match 10-15')),
            ('match 15-20', _('match 15-20')),
            ('match 20-25', _('match 20-25')),
            ('match 25-30', _('match 25-30')),
            ('match 30-35', _('match 30-35')),
            ('match 35-40', _('match 35-40')),
            ('match 40-45', _('match 40-45')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'match 1-5':
            return queryset.filter(number__gte=1, number__lte=5)
        if self.value() == 'match 5-10':
            return queryset.filter(number__gte=5, number__lte=10)
        if self.value() == 'match 10-15':
            return queryset.filter(number__gte=10, number__lte=15)
        if self.value() == 'match 15-20':
            return queryset.filter(number__gte=15, number__lte=20)
        if self.value() == 'match 20-25':
            return queryset.filter(number__gte=20, number__lte=25)
        if self.value() == 'match 25-30':
            return queryset.filter(number__gte=25, number__lte=30)
        if self.value() == 'match 30-35':
            return queryset.filter(number__gte=30, number__lte=35)
        if self.value() == 'match 35-40':
            return queryset.filter(number__gte=35, number__lte=40)
        if self.value() == 'match 40-45':
            return queryset.filter(number__gte=40, number__lte=45)

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'
    search_fields = ('title',)

class GroupstageModelAdmin(ModelAdmin):
    model = GroupstageTournamentModel
    menu_label = 'Gruppenphase'
    menu_icon = 'fa-user-times'
    list_display = ('number', 'starts_at',
        'team_1_dress', 'team_1', 'team_1_total_score', 'team_1_total_points',
        'team_2_total_points', 'team_2_total_score', 'team_2', 'team_2_dress')
    list_per_page = 10
    list_filter = (MaxFiveMatchFilter, 'starts_at')
    search_fields = ('number', 'starts_at')

class ScreencastPageModelAdmin(ModelAdmin):
    model = ScreencastPage
    menu_label = 'Presentation Screen'
    menu_icon = 'fa-desktop'

class TreichleCupModelAdmin(ModelAdminGroup):
    menu_label = 'Treichle-Cup'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (
        TeamRoosterModelAdmin,
        GroupstageModelAdmin,
        ScreencastPageModelAdmin
    )

modeladmin_register(TreichleCupModelAdmin)



class NewsModelAdmin(ModelAdmin):
    model = NewsPage
    menu_label = 'News'
    menu_icon = 'edit'
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', 'date_published', 'last_modified')
    list_filter = ('date_published', 'last_modified')
    search_fields = ('title',)

modeladmin_register(NewsModelAdmin)
