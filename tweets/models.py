from django.db import models
from common.models import CommonModel


class Tweet(CommonModel):
    """ Tweet Model Definition """

    payload = models.CharField(max_length=180)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.payload
    
    def like_count(self):
        return self.likes.count()


class Like(CommonModel):
    """ Like Model Definition """

    user = models.ForeignKey('users.User', related_name='likes', ordn_delete=models.CASCADE)
    tweet = models.ForeignKey('tweets.Tweet', related_name='likes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tweet.payload}"
