# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster, Teams

class TeamsModelAdmin(ModelAdmin):
    model = Teams
    menu_label = 'Add Teams Page'
    menu_icon = 'plus'

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'

class TreichleCupModelAdmin(ModelAdminGroup):
    menu_label = 'Treichle-Cup'
    menu_icon = 'folder-open-inverse'
    menu_order = 200
    items = (TeamsModelAdmin, TeamRoosterModelAdmin)

modeladmin_register(TreichleCupModelAdmin) 
