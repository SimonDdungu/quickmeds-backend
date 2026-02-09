from rest_framework.decorators import api_view
from rest_framework.response import Response
from inventory.models.medicine import DOSAGE_FORMS, STRENGTH_UNITS

@api_view(['GET'])
def dosage_form_list(request):
    data = [{'value': value, "label": dosage} for value, dosage in DOSAGE_FORMS]
    return Response(data)

@api_view(['GET'])
def strength_unit_list(request):
    data = [{'value': value, "label": strength_unit} for value, strength_unit in STRENGTH_UNITS]
    return Response(data)