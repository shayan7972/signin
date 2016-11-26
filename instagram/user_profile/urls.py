from django.conf.urls import url

from user_profile.views import profile, following, follower

urlpatterns = [
    url(r'^[a-zA-Z0-9_.]{4,}/',profile),
    url(r'^[a-zA-Z0-9_.]{4,}/follower',follower),
    url(r'^[a-zA-Z0-9_.]{4,}/following',following)
]
