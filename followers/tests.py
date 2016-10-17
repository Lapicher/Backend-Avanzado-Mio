from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from followers.models import Relationship
from followers.utils import get_followers, get_following


class RelationshipTests(TestCase):

    def test_get_followers_returns_users_that_follow_by_a_given_user(self):

        user1= User.objects.create_user("luke", "skywalker@starwars.com","skywalker")
        user2= User.objects.create_user("anakin", "annie@starward.com", "anakinSky")

        Relationship.objects.create(origin=user1, target=user2) #usuario 1 sigue a usuario2


        followers = get_followers(user2)

        self.assertEqual([user1], followers) # followers == [user1]



    def test_get_following_returns_users_that_a_given_user_follows(self):

        user1 = User.objects.create_user("luke", "skywalker@starwars.com", "skywalker")
        user2 = User.objects.create_user("anakin", "annie@starward.com", "anakinSky")

        Relationship.objects.create(origin=user1, target=user2)  # usuario 1 sigue a usuario2

        following = get_following(user1)

        self.assertEqual([user2], following)  # followers == [user1]


