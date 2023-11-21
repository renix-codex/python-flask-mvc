from models import User, Post, Comment

# Dummy data
users = [
    User(user_id=1, username='john_doe', email='john@example.com', password='password123'),
    User(user_id=2, username='jane_smith', email='jane@example.com', password='securepass')
]

posts = [
    Post(post_id=1, title='Introduction to Flask MVC', content='...', author=users[0]),
    Post(post_id=2, title='Building a Blog with Flask', content='...', author=users[1])
]

comments = [
    Comment(comment_id=1, content='Great post!', author=users[2]),
    Comment(comment_id=2, content='I have a question...', author=users[3])
]

def get_user_by_username(username):
    return next((user for user in users if user.username == username), None)

def get_post_by_id(post_id):
    return next((post for post in posts if post.post_id == post_id), None)

def get_comments_for_post(post):
    return [comment for comment in comments if comment.post == post]
