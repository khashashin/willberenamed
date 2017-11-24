from django.db import models

# Create your models here.
class Staff(models.Model):
    team_name = models.CharField(max_length=100, default="")
    staff_name = models.CharField(max_length=100, default="")
    staff_vorname = models.CharField(max_length=100, default="")
    staff_position = models.CharField(max_length=100, default="")
    foto = models.URLField(max_length=255, default="")

class TeamRooster(models.Model):
    sp_nr = models.IntegerField()
    sp_name = models.CharField(max_length=100, default="")
    sp_vorname = models.CharField(max_length=100, default="")
    sp_pos = models.CharField(max_length=100, default="")
    sp_jahrgang = models.IntegerField()
    sp_foto = models.URLField(max_length=255, default="")
