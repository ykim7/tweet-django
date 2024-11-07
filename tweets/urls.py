from django.urls import path
from .views import tweet_list, user_tweet_list

urlpatterns = [
    path("api/v1/tweets/", tweet_list, name="tweet-list"),
    path("api/v1/users/<int:user_id>/tweets", user_tweet_list, name="user-tweet-list"),
]
