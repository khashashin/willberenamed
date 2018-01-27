from django import template
from team_rooster.constanten import POSITIONS_LOOKUP, POSITIONS_SP_LOOKUP

register = template.Library()

@register.simple_tag
def get_position_display_name(name):
    return POSITIONS_LOOKUP.get(name)

@register.simple_tag
def get_position_sp_display_name(name):
    return POSITIONS_SP_LOOKUP.get(name)
