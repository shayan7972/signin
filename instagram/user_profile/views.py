from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, 'user_profile/homepage.html')
def follower(request):
    pass
def following(request):
    pass