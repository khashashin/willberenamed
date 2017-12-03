# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from .models import TeamRooster

######################################################
#################### Sidebar Menu ####################
######################################################

# class TeamRoosterModelAdmin(ModelAdmin):
#     model = TeamRooster
#     menu_icon = 'form'

######################################################
########## Settings Menu Permanent Daten #############
######################################################

# class TreichleCupModels(ModelAdminGroup):
#     menu_label = 'Treichle-Cup'
#     menu_icon = 'folder-open-inverse'
#     menu_order = 200
#     items = TeamRoosterModelAdmin
#
# modeladmin_register(TreichleCupModels)
