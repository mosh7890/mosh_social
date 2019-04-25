from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialAccountListView
from rest_auth.views import UserDetailsView


class MyFacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class MyUserDetailsView(UserDetailsView):
    """
    Return User.
    """


class MySocialAccountListView(SocialAccountListView):
    """
    List Social Accounts
    """


MyFacebookLogin = MyFacebookLogin.as_view()
MyUserDetailsView = MyUserDetailsView.as_view()
MySocialAccountListView = MySocialAccountListView.as_view()
