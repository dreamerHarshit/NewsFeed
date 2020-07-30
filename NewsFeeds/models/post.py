from datetime import datetime


class Post:
    id_count = 1
    post_id = 0
    score = 0
    downvote = 0
    upvote = 0
    comment_count = 0
    posted_by = None
    posted_on = None

    def __init__(self, content, posted_by):
        self.post_id = Post.id_count
        Post.id_count += 1
        self.posted_by = posted_by
        self.posted_on = datetime.now()
        self.content = content

    def get_content(self):
        return self.content

    def get_comment_count(self):
        return self.comment_count

    def increment_comment_count(self):
        self.comment_count += 1

    def set_upvote(self):
        self.upvote += 1
        self.update_score()

    def set_downvote(self):
        self.downvote += 1
        self.update_score()

    def update_score(self):
        self.score = self.upvote - self.downvote

    def get_score(self):
        return self.score

    def get_posted_on(self):
        return self.posted_on
