from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from rest_framework import serializers, viewsets, routers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# This would be served from a database normally.
# However, as we probably won't use one, this demo shows in-memory data.
NUMBERS = {1002: {"id": 1002, "name": "One Thousand and two"},
           39949: {"id": 39949, "name": "Thirty-nine thousand, nine hundred and forty nine"},
           55: {"id": 55, "name": "Fiffty-five"},
           28: {"id": 28, "name": "Twenty-eight"}}


# Friendly greeting.

def home(request):
    return HttpResponse("Hello, world.")


# Naive JSON API
# Just to show it's doable.

def naive_numbers(request):
    return JsonResponse({'numbers': NUMBERS})

def naive_number(request, num_id):
    number_data = NUMBERS[num_id]
    try:
      number_data = NUMBERS[num_id]
      return JsonResponse({'number': number_data})
    except KeyError:
      raise Http404("Number does not exist!")

# Numbers using Using REST API

# The objects we're dealing with.
class Number(object):
    def __init__(self, data):
        self.num_id = data["id"]
        self.num_name = data["name"]

# For auto API and schema generation.
class NumberSerializer(serializers.Serializer):
    num_id = serializers.IntegerField()
    num_name = serializers.CharField()

class NumberViewSet(viewsets.ViewSet):
    serializer_class = NumberSerializer

    def list(self, request):
        # Construct an object for each.
        nums = [Number(x) for x in NUMBERS.values()]

        serializer = NumberSerializer(nums, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # Look up and construct.
        number = Number(NUMBERS[int(pk)])

        serializer = NumberSerializer(number)
        return Response(serializer.data)


# Attach the endpoints.
numbers_router = routers.DefaultRouter()
numbers_router.register(r'numbers', NumberViewSet, basename='number')

