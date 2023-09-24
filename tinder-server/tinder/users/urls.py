from django.contrib import admin
from django.urls import path
from users.views import login, logout, UserRegistrationView, UserProfileView
from django.contrib.auth.decorators import login_required

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', login(UserRegistrationView.as_view()), name='registration'),
    path('profile/<int:pk>', UserProfileView.as_view(), name='profile'),

]

