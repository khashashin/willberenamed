# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster
from news.models import NewsPage
from matches.models import MatchPage

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)

modeladmin_register(TeamRoosterModelAdmin)

class NewsModelAdmin(ModelAdmin):
    model = NewsPage
    menu_label = 'News'
    menu_icon = 'edit'
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)

class MatchesModelAdmin(ModelAdmin):
    model = MatchPage

modeladmin_register(NewsModelAdmin)
