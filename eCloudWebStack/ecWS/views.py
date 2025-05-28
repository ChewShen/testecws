from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
import traceback


from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def registerPage(request):
    return render(request, 'registerPage.html',{})

def loginPage(request):
    return render(request, 'loginPage.html',{})

@login_required
def dashboard(request):
    email = request.user.email  # fallback if stored on User model

    try:
        social_account = SocialAccount.objects.get(user=request.user)
        extra_data = social_account.extra_data
        email = extra_data.get('email', email)  # prefer Google email if available
        first_name = extra_data.get('given_name', '')
        last_name = extra_data.get('family_name', '')
    except SocialAccount.DoesNotExist:
        first_name = ''
        last_name = ''

    return render(request, 'dashboard.html', {
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
    })