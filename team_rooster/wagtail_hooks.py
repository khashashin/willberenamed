# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster
from news.models import NewsPage

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    search_fields = ('title',)

modeladmin_register(TeamRoosterModelAdmin)

class NewsModelAdmin(ModelAdmin):
    model = NewsPage
    menu_label = 'News'
    menu_icon = 'edit'
    menu_order = 300  # will put in 3rd place (000 being 1st, 100 2nd)
    list_display = ('title', 'date_published', 'last_modified')
    list_filter = ('date_published', 'last_modified')
    search_fields = ('title',)

modeladmin_register(NewsModelAdmin)
