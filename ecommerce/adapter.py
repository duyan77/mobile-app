from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from store.models import User

class NoSignupAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return False

class NoSignupSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, sociallogin):
        return True

    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        user.email = sociallogin.account.extra_data['email']
        user.first_name = sociallogin.account.extra_data.get('given_name', '')
        user.last_name = sociallogin.account.extra_data.get('family_name', '')
        # Save avatar if available
        
       
        user.avatar_url = 'https://png.pngtree.com/png-vector/20220709/ourmid/pngtree-businessman-user-avatar-wearing-suit-with-red-tie-png-image_5809521.png'
        user.save()

        # avatar_url = sociallogin.account.extra_data.get('picture','')
        # if avatar_url:
        #     user.avatar_url = avatar_url            
        # user.save()

        return user