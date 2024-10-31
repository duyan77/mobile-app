from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from store.models import User

class NoSignupAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True

class NoSignupSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return True

    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        user.email = sociallogin.account.extra_data['email']
        user.first_name = sociallogin.account.extra_data.get('given_name', '')
        user.last_name = sociallogin.account.extra_data.get('family_name', '')
        user.username = sociallogin.account.extra_data['email']
        if sociallogin.account.provider == 'google':
            user.avatar_url = sociallogin.account.extra_data.get('picture', '')
        else:
            user.avatar_url = 'https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png'
        user.save()
        return user