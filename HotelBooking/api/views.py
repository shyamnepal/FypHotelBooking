from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from .models import Signup

from .serializer import SignUpSerializers
from rest_framework.response import Response


@api_view(['GET'])
def showall(request):
    personal_details = Signup.objects.all()
    serializers = SignUpSerializers(personal_details, many=True)
    return Response(serializers.data)

