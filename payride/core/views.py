from os import stat
from rest_framework.views import APIView
from core import serializers as core_serializer
from core import models as core_models
from rest_framework.response import Response
from rest_framework import status


class Register(APIView):
    def post(self, request):
        serialize_data = core_serializer.Register(data = request.data)

        if not serialize_data.is_valid():
            return Response(serialize_data.errors, status = status.HTTP_400_BAD_REQUEST)
        
        serialize_data = serialize_data.validated_data

        data = core_models.User.objects.filter(
            name = serialize_data.get("name"),
            email = serialize_data.get("email"),
            phone = serialize_data.get("phone"),
            password = serialize_data.get("password"),
            role = serialize_data.get("role"),
        )
        if data:
            return Response({'message':'Already Existed'},status = status.HTTP_200_OK)

        core_models.User.objects.create(
            name = serialize_data.get("name"),
            email = serialize_data.get("email"),
            phone = serialize_data.get("phone"),
            password = serialize_data.get("password"),
            role = serialize_data.get("role"),
        )

        return Response({'message':'Done'},status = status.HTTP_201_CREATED)


class Login(APIView):
    def post(self, request):
        serialize_data = core_serializer.Login(data = request.data)

        if not serialize_data.is_valid():
            return Response(serialize_data.errors, status = status.HTTP_400_BAD_REQUEST)

        print(serialize_data)

        serialize_data = serialize_data.data

        data = core_models.User.objects.filter(
            email = serialize_data.get("email"),
            password = serialize_data.get("password")
        ).last()

        print(data.uuid)
        if data:
            request.session['uid'] = str(data.uuid)
            return Response({'message':'Login!'},status = status.HTTP_200_OK)
        else:
            return Response({'message':'Account Doesnt Exist'},status = status.HTTP_401_UNAUTHORIZED)
