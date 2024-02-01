from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'role',
                  'created_at', 'password', 'password2']
        extra_kwagrs = {
            'password': {'write_only': True},
            'password2': {'write_only': True}
        }

    def create(self, validated_data):
        full_name = validated_data.get('full_name')
        phone_number = validated_data.get('phone_number')
        role = validated_data.get('role')
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password == password2:
            user = User(
                full_name=full_name,
                phone_number=phone_number,
                role=role,
            )
            user.set_password(password)
            user.save()
            return user
        else:
            raise serializers.ValidationError(
                {
                    'error': 'Both passwords do not match'
                }
            )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['full_name', 'phone_number', 'role', 'created_at']
