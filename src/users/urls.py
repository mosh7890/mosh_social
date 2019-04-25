from django.urls import path

from .views import MyFacebookLogin, MyUserDetailsView, MySocialAccountListView

app_name = 'users'
urlpatterns = [
    path('rest-auth/facebook/', MyFacebookLogin, name='rest_facebook'),
    path('rest-auth/user/', MyUserDetailsView, name='rest_user_details'),
    path('rest-auth/social-list/', MySocialAccountListView, name='rest_social_list'),
]
