from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    School = models.CharField(max_length=60)
    District =  models.CharField(max_length=46)
    DistID = models.IntegerField()

class Performance(models.Model):
    School = models.CharField(max_length=60)
    District =  models.CharField(max_length=46)
    DistrictID = models.IntegerField()
    SchoolID = models.IntegerField()
    AcademicYear = models.IntegerField()
    Subject = models.CharField(max_length=21)
    Subgroup = models.CharField(max_length=32)
    GradeLevel = models.CharField(max_length=3)
    ParticipationRate2014to2015 = models.FloatField()
    PercentageMeetsORExceeds2014to2015 = models.FloatField()
