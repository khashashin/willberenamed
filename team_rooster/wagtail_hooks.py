# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from . models import TeamRooster

class TeamRoosterModelAdmin(ModelAdmin):
    model = TeamRooster
    menu_label = 'Treichle Cup'
    menu_icon = 'group'
    menu_order = 200
    exclude_from_explorer = True

modeladmin_register(TeamRoosterModelAdmin)
