class UserFollowers:
    user_followers = {}

    def __init__(self):
        return

    def get_followers(self, name):
        return self.user_followers[name]

    def add_follower(self, name, following):
        if name in self.user_followers.keys():
            self.user_followers[name].append(following)
        else:
            self.user_followers[name] = []
            self.user_followers[name].append(following)