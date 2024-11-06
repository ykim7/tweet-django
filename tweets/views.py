from django.shortcuts import render
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.all() 
    return render(request, 'tweet_list.html', {'tweets': tweets})