from rest_framework import serializers

class Register(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=200)
    role = serializers.CharField(max_length=10)

class VerifyEmail(serializers.Serializer):
    email = serializers.EmailField()

class Login(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)

class AddTrip(serializers.Serializer):
    to = serializers.CharField(max_length = 200)
    destination = serializers.CharField(max_length = 200)
    start_time = serializers.TimeField(format='%I:%M %p', input_formats='%I:%M %p')
    end_time = serializers.TimeField(format='%I:%M %p', input_formats='%I:%M %p')
