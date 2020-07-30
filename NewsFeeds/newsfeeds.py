from models.user import User
from models.post import Post
from models.post_comments import PostComments
from models.user_follower import UserFollowers


class NewsFeed:
    posts = {}
    users = {}
    user_follower = UserFollowers()
    posts_id = {}

    def __init__(self):
        self.current_user = None

    def set_current_user(self, user):
        self.current_user = user

    def signup(self, name):
        user = User(name)
        self.users[name] = user

    def signin(self, name):
        if name in self.users.keys():
            self.set_current_user(self.users[name])
            print("Signin successfull")
            return
        print("User does not exist!")

    def add_post(self, content):
        post = Post(content, self.current_user)
        if self.current_user in self.posts.keys():
            self.posts[self.current_user].append(post)
            self.posts_id[post.post_id] = post
        else:
            self.posts[self.current_user] = []
            self.posts[self.current_user].append(post)
            self.posts_id[post.post_id] = post

    def compare_posts(self, p1, p2):
        if p1.get_score() != p2.get_score():
            return p1.get_score() < p2.get_score()
        elif p1.get_comment_count() != p2.get_comment_count():
            return p1.get_comment_count() < p2.get_comment_count()
        else:
            return p1.get_posted_on() < p2.get_posted_on()

    def show_news_feed(self):
        if self.current_user is not None:
            users = self.user_follower.get_followers(self.current_user)
            posts = []
            for u in users:
                for p in self.posts.get(u):
                    posts.append(p)
            posts = sorted(posts, key=lambda x: (x.score, x.comment_count, x.posted_on), reverse=True)
            for p in posts:
                print str(p.post_id) + "\n"
                print p.posted_on.strftime("%d/%m/%Y, %H:%M:%S") + "\n"
                print p.posted_by.name + "\n"
                print(str(p.upvote), str(p.downvote))
                print "\n" + p.content + "\n"

    def follow(self, name):
        following = self.users[name]
        self.user_follower.add_follower(self.current_user, following)

    def upvote(self, id):
        import pdb;pdb.set_trace()
        post = self.posts_id[int(id)]
        post.set_upvote()

    def downvote(self, id):
        post = self.posts_id[int(id)]
        post.set_downvote()

    def reply(self, id):
        pass