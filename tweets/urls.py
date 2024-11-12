from django.urls import path
from .views import TweetList, UserTweetList

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/tweets/", include("tweets.urls")),
    path("api/v1/users/", include("users.urls")),
]