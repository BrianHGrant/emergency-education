from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from education.models import School
from education.serializers import SchoolSerializer, PerformanceSerializer

@api_view(['GET', 'POST'])
def school_list(request, format=None):
    """
    List all snippets, or create a new film.
    """
    if request.method == 'GET':
        schools = School.objects.all()
        serializedSchool = SchoolSerializer(schools, many=True)
        return Response(serializedSchool.data)

    elif request.method == 'POST':
        serializedSchool = SchoolSerializer(data=request.data)
        if serializedSchool.is_valid():
            serializedSchool.save()
            return Response(serializedSchool.data, status=status.HTTP_201_CREATED)
        return Response(serializedSchool.errors, status=status.HTTP_400_BAD_REQUEST)
