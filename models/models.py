class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

class Post:
    def __init__(self, post_id, title, content, author):
        self.post_id = post_id
        self.title = title
        self.content = content
        self.author = author
        self.comments = []

class Comment:
    def __init__(self, comment_id, content, author):
        self.comment_id = comment_id
        self.content = content
        self.author = author
