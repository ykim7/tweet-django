from django.contrib import admin
from .models import Tweet, Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ['payload', 'user', 'like_count']
    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Likes Count'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
