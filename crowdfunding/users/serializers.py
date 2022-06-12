from rest_framework import serializers
from .models import CustomUser

# TRY SIMPLIFY THIS IN THE FUTURE BY USING serializers.ModelSerializer

# User Serializer
# class CustomUserSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     username = serializers.CharField(max_length=200)
#     email = serializers.CharField(max_length=200)
#     profile_pic = serializers.URLField()

#     def create(self, validated_data):
#           return CustomUser.objects.create(**validated_data)


# User Serializer
class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'profile_pic']

    def create(self, validated_data):
          return CustomUser.objects.create(**validated_data)

# Register User
class RegisterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'email', 'profile_pic']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

# Edit User Serializer
class CustomUserDetailSerializer(CustomUserSerializer):
    
    def update(self, instance, validated_data):
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.save()
        return instance