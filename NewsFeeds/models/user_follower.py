class UserFollowers:
    user_followers = {}

    def __init__(self):
        return

    def get_followers(self, name):
        return UserFollowers.user_followers[name]

    def add_follower(self, name, following):
        if name in UserFollowers.user_followers.keys():
            UserFollowers.user_followers[name].append(following)
        else:
            UserFollowers.user_followers[name] = []
            UserFollowers.user_followers[name].append(following)
