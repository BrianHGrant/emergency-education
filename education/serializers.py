from rest_framework import serializers
from education.models import School, Perfomance

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'School', 'District', 'DistID')

class PerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Performance
        fields = ('id', 'School', 'SchoolID' 'District', 'DistID', 'AcademicYear', 'Subject', 'Subgroup', 'GradeLevel', 'ParticipationRate2014to2015', 'PercentageMeetsORExceeds2014to2015')
