from django.shortcuts import render
from .models import Tweet
from users.models import User
from rest_framework.exceptions import NotFound


def tweet_list(request):
    tweets = Tweet.objects.all()
    return render(
        request,
        "tweet_list.html",
        {"tweets": tweets},
    )


def user_tweet_list(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        tweets = Tweet.objects.filter(user=user)
        data = []
        for tweet in tweets:
            each_tweet = {
                "id": tweet.id,
                "payload": tweet.payload,
                "user_id": tweet.user.id,
            }
            data.append(each_tweet)
        return render(request, "user_tweet_list.html", {"tweets": tweets, "user": user})
    except User.DoesNotExist:
        return NotFound
