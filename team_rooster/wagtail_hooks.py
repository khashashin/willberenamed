# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from . models import TeamRooster

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Team Manager'
    menu_icon = 'group'
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)

modeladmin_register(TeamRoosterModelAdmin)
