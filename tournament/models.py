from django.db import models
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
)
from wagtail.wagtailcore.fields import StreamField

from team_rooster.models import TeamRooster
from matches.models import MatchPage
