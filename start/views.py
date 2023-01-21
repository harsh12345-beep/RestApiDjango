from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,APIView

from rest_framework.response import Response

from  start.models import details
from  .serializer import detailsserializer
from rest_framework import status

# @api_view(['POST'])
# def index(request):
#     try:
#        detail = details.objects.all()
#        serializer = detailsserializer(detail, many=True)
#        print(serializer.data)
#        return Response(serializer.data)
#     except:
#         print("failed")


class Pract(APIView):
     def post(self, request, *args, **kwargs):
            data = {
            'name': request.data.get('name'), 
            'course': request.data.get('course'),
        }
            serializer = detailsserializer(data=data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

