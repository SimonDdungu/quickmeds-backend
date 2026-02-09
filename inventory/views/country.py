from rest_framework.decorators import api_view
from rest_framework.response import Response
from inventory.constants import COUNTRIES

@api_view(['GET'])
def countries_list(request):
    data = [{"value": code, "label": name} for code, name in COUNTRIES]
    return Response(data)