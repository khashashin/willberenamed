from django.shortcuts import render
from .models import TeamRooster
# Create your views here.
def teams(request):
    teams = TeamRooster.objects.all()
    return render(request, 'team_rooster.html', { 'teams': teams})
