from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home_view(request):
    if request.user.is_authenticated:
        return redirect("account_profile")
    return render(request, "home.html")

@login_required
def profile_view(request):
    return render(request, "account/profile.html")
