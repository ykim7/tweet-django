from rest_framework.test import APITestCase
from .models import Tweet
from users.models import User


class TestTweets(APITestCase):

    URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        self.user = user

        Tweet.objects.create(payload="Test Tweet 1", user=self.user)
        Tweet.objects.create(payload="Test Tweet 2", user=self.user)

    def test_get_all_tweets(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["payload"], "Test Tweet 1")
        self.assertEqual(data[1]["payload"], "Test Tweet 2")

    def test_create_tweet(self):
        self.client.force_login(self.user)

        response = self.client.post(
            self.URL,
            data={"payload": "New Test Tweet", "user": self.user.id},
        )
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["payload"], "New Test Tweet")
        self.assertEqual(data["user"], self.user.id)

    def test_create_tweet_unauthenticated(self):
        response = self.client.post(self.URL, data={"payload": "New Test Tweet"})
        self.assertEqual(response.status_code, 403)


class TestTweetDetail(APITestCase):

    base_URL = "/api/v1/tweets/"

    def setUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("12345")
        user.save()
        self.user = user

        tweet = Tweet.objects.create(payload="Test Tweet", user=self.user)
        self.tweet = tweet
    
    def test_tweet_not_found(self):
        response = self.client.get("/api/v1/tweets/{self.tweet.id}/2")

        self.assertEqual(response.status_code, 404)

    def test_get_tweet(self):
        response = self.client.get(f"/api/v1/tweets/{self.tweet.id}/")
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["payload"], "Test Tweet")
        self.assertEqual(data["user"], self.user.id)

    def test_update_tweet(self):
        self.client.force_login(self.user)

        response = self.client.put(
            f"/api/v1/tweets/{self.tweet.id}/",
            data={"payload": "Updated Tweet", "user": self.user.id},
        )
        data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["payload"], "Updated Tweet")

    def test_delete_tweet(self):
        self.client.force_login(self.user)

        response = self.client.delete(f"/api/v1/tweets/{self.tweet.id}/")

        self.assertEqual(response.status_code, 204)

        response = self.client.get(f"/api/v1/tweets/{self.tweet.id}/")
        self.assertEqual(response.status_code, 404)
