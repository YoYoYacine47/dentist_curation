from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, authentication
from clinics.models import Clinic
from clinics.serializers import ClinicSerializer
from patients.models import ProblemDetected, Visit
from patients.serializers import ProblemDetectedSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    data = request.data
    print(data)
    # visits = Visit.objects.filter(
    #     timestamp__date__gte=data.from_date, timestamp__date__lte=data.to_date)
    ProblemDetected.objects.filter()
    problem = ProblemDetected.objects.all()
    print(problem)
    data = ProblemDetectedSerializer(problem, many=True).data
    return Response(data)


class ClinicListAPIView(generics.ListAPIView):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]
