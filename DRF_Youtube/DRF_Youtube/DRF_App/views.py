from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegisterSerializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# Create your views here.
class register(APIView):

    def post(self,request,format=None):
        serializers = UserRegisterSerializers(data=request.data)
        data = {}
        if serializers.is_valid():
            account = serializers.save()
            data['response'] = 'registered'
            data['username'] = account.username
            data['email'] = account.email
            token,create = Token.objects.get_or_create(user=account)
            data['token'] = token.key
            
        else:
            data = serializers.errors
        return Response(data)   
        
