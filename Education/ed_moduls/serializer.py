from rest_framework.serializers import ModelSerializer
from .models import EducationModul

class EducationModulSerializer(ModelSerializer):
    class Meta:
        model = EducationModul
        fields = '__all__' # serializ all fields our models

