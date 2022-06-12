from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django.core.exceptions import ObjectDoesNotExist

# Token Auth Imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Permission Import
from .permissions import IsOwnerOrReadOnly

# Model Import
from .models import CustomUser

# Serializer Import
from .serializers import CustomUserSerializer, CustomUserDetailSerializer, RegisterSerializer



# Give a new user a token and id
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# TRY SIMPLIFY THIS IN THE FUTURE BY USING generics.ListAPIView and generics.RetrieveUpdateDestroyAPIView

# Display a list of all users
class CustomUserList(APIView):

    def get(self, request):
          users = CustomUser.objects.all()
          serializer = CustomUserSerializer(users, many=True)
          return Response(serializer.data)

# Create a User
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            user = serializer.data['id']
            token, created = Token.objects.get_or_create(user_id=user)
            return Response({
                'token': token.key,
                'data': serializer.data
            })
        return Response(serializer.errors)


# Display a single user and allow them to edit
class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        data = request.data
        serializer = CustomUserDetailSerializer(
            instance=user,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# User Logout
class UserLogout(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        logout(request)

        return Response({"success": _("Successfully logged out.")},
                        status=status.HTTP_200_OK)

# Register View
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny,]
    queryset = CustomUser.objects.all()

