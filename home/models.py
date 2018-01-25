from __future__ import absolute_import, unicode_literals

from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.wagtailadmin.edit_handlers import (
    PageChooserPanel,
)

from wagtail.wagtailcore.models import Page


class HomePage(Page):

    teams_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Choose ',
        help_text='Choose a page to link to for the Team Rooster Page'
    )

    subpage_types = ['news.NewsPage']
    parent_page_types = ['wagtailcore.Page']

    content_panels = [
        PageChooserPanel('teams_page'),
    ]

    def get_news(self):
        return news.NewsPage.objects.live().descendant_of(
            self).order_by('-first_published_at')

    def children(self):
        return self.get_children().specific().live()

    def paginate(self, request, *args):
        page = request.GET.get('page')
        paginator = Paginator(self.get_news(), 12)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)
        return pages

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        return context
