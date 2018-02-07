# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster
from news.models import NewsPage
# from matches.models import MatchPage
from tournament.models import (
    GroupstageTournamentModel, FinalphaseTournamentModel,
    TournamentPage, ScreencastPage)

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'
    search_fields = ('title',)

class TournamentModelAdmin(ModelAdmin):
    model = TournamentPage
    menu_label = 'Tournament'
    menu_icon = 'fa-trophy'
    list_display = ('starts_at', 'ends_at')
    list_per_page = 5
    search_fields = ('title', 'starts_at')

class GroupstageModelAdmin(ModelAdmin):
    model = GroupstageTournamentModel
    menu_label = 'Gruppenphase'
    menu_icon = 'fa-user-times'
    list_display = ('number', 'starts_at',
        'team_1_dress', 'team_1', 'team_1_total_score', 'team_1_total_points',
        'team_2_total_points', 'team_2_total_score', 'team_2', 'team_2_dress')
    list_per_page = 10
    list_filter = ('number', 'starts_at')
    search_fields = ('number', 'starts_at')

class FinalstageModelAdmin(ModelAdmin):
    model = FinalphaseTournamentModel
    menu_label = 'Finalphase'
    menu_icon = 'fa-user-plus'
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
        TournamentModelAdmin,
        GroupstageModelAdmin,
        FinalstageModelAdmin,
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
