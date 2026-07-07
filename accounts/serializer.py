from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.Serializer):
    phone     = serializers.CharField(max_length=11)
    full_name = serializers.CharField(max_length=255)
    email     = serializers.EmailField()
    password  = serializers.CharField(write_only=True, min_length=6)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("this email already exists.")
        return value

    def validate_phone(self, value):
        if User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("this phone number already exists.")


class VerifySerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'