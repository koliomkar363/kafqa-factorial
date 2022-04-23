import math
from django.http import HttpResponse


def index(request, num):
    result = math.factorial(num)
    return HttpResponse(result)
