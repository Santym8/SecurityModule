from rest_framework import serializers

class LoginRequest(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField()