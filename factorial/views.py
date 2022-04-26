import math
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request, input):
    try:
        num = int(input)
    except ValueError:
        return Response("Error: Invalid number!", status=status.HTTP_400_BAD_REQUEST)

    if num < 0:
        return Response("Error: Invalid number!", status=status.HTTP_400_BAD_REQUEST)

    result = math.factorial(num)
    return Response(result)
