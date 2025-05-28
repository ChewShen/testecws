from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.admin import SocialAccountAdmin  # The default admin
from django.utils.html import format_html
# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(SocialAccount)
class userAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","email"]


# Create a custom admin for SocialAccount
class CustomSocialAccountAdmin(SocialAccountAdmin):
    list_display = ('user', 'get_full_name', 'get_email', 'provider')

    # Custom method to get the full name
    def get_full_name(self, obj):
        # Get full name from extra_data (first_name + last_name)
        first_name = obj.extra_data.get('given_name', '')
        last_name = obj.extra_data.get('family_name', '')
        return format_html(f"{first_name} {last_name}")
    
    get_full_name.short_description = 'Full Name'  # Column title
    
    # Custom method to get email from extra_data
    def get_email(self, obj):
        # Get the email from extra_data
        return obj.extra_data.get('email', obj.user.email)  # Fallback to the user's email if not found
    
    get_email.short_description = 'Email'  # Column title

# Register the custom admin for SocialAccount
admin.site.register(SocialAccount, CustomSocialAccountAdmin)
admin.site.unregister(User)
admin.site.register(User, userAdmin)
admin.site.register(Profile)