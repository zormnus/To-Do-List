from django.urls import path
from .views import UserAuthView, UserRegView, UserLogoutView, UserUpdateView, ProfileView

app_name = 'users'

urlpatterns = [
    path('auth/', UserAuthView.as_view(), name='auth'),
    path('reg/', UserRegView.as_view(), name='reg'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]