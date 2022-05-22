from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """ Test API View """
    serializer_class = serializers.HelloSerializer

    def get (self,request,format=None):
        """ Returns a list of API view Features"""
        an_apiview = [
            'uses http methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional django view'
            'Gives you the most control over your application logic '
            'Is mapped manually to urls '
        ]

        return Response({'message':'Helloo!!' , 'an_apiview': an_apiview})

    def post (self,request):
        """ Create hello message with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "hello" + name
            return Response ({'message':message})
        else:
            return Response (serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def put (self,request,pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self,requesst,pk=None):
        """Handles partial updating object"""
        return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({"method":"DELETE"})         
