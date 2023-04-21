from django.test import TestCase
from ed_moduls.models import EducationModul

class EducationModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        EducationModul.objects.create(name="Python", description="Django_REST")

    def test_name(self):
        #check the verbose_name of fields 
        name_field = ("name", "description")
        modul = EducationModul.objects.get(id=1)
        for el in name_field:
            field_label = modul._meta.get_field(el).verbose_name
            self.assertEqual(field_label, el)

    def test_max_length(self):
        # check the max length for fields in model
        field_length = {"name": 64, "description": 250}
        modul = EducationModul.objects.get(id=1)
        for key, value in field_length.items():
            max_length = modul._meta.get_field(key).max_length
            self.assertEqual(max_length, value)
        