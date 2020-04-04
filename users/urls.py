from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from users import views as user_views
from .views import UserDetailView, UserListView


urlpatterns = [
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', user_views.profile, name="profile"),
    path('list/', UserListView.as_view(), name="user-list"),
    path('<int:pk>', UserDetailView.as_view(), name="user-detail")
]