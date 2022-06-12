from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('authenticate/', views.CustomObtainAuthToken.as_view()),
    path('users/', views.CustomUserList.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view()),
    path('users/logout/', views.UserLogout.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)