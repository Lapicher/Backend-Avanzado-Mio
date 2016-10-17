from followers.models import Relationship


def get_followers(user):

    relationships = Relationship.objects.filter(target=user)
    followers = list()
    for relationship in relationships:
        followers.append(relationship.origin)

    return followers


def get_following(user):
    relationships = Relationship.objects.filter(origin=user)
    following= list()

    for relationship in relationships:
        following.append(relationship.target)

    return following