from rest_framework import serializers
from .models import CustomUser

# TRY SIMPLIFY THIS IN THE FUTURE BY USING serializers.ModelSerializer

# User Serializer
class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    profile_pic = serializers.URLField()

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)



class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data):
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.save()
        return instance