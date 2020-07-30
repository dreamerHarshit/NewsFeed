class PostComments:
    post_comments = {}

    def get_comments(self, post_id):
        return PostComments.post_comments.get(post_id)

    def add_comment(self, comment, post):
        if post.post_id in PostComments.post_comments.keys():
            PostComments.post_comments[post.post_id].append(comment)
        else:
            PostComments.post_comments[post.post_id] = []
            PostComments.post_comments[post.post_id].append(comment)
        post.increment_comment_count()
