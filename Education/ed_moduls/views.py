from rest_framework.viewsets import ModelViewSet
from .models import EducationModul
from .serializer import EducationModulSerializer

class EducationModulViewSet(ModelViewSet):
    serializer_class = EducationModulSerializer
    queryset = EducationModul.objects.all()







