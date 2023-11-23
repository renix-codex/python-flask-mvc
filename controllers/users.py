from flask import jsonify
from models import User, Post

# Dummy data
users = [
    User(user_id=1, username='john_doe', email='john@example.com', password='password123'),
    User(user_id=2, username='jane_smith', email='jane@example.com', password='securepass')
]

posts = [
    Post(post_id=1, title='Introduction to Flask MVC', content='...', author=users[0]),
    Post(post_id=2, title='Building a Blog with Flask', content='...', author=users[1])
]


def get_user_by_username(username):
    return next((user for user in users if user.username == username), None)

def list_all_users():
    user_list = [user.__dict__ for user in users]
    return user_list

def get_post_by_id(post_id):
    post = next((post for post in posts if post.post_id == post_id), None)
    if post:
        return post_to_dict(post)
    return None

def post_to_dict(post):
    return {
        'post_id': post.post_id,
        'title': post.title,
        'content': post.content,
        'author': user_to_dict(post.author)
    }

def user_to_dict(user):
    return {
        'user_id': user.user_id,
        'username': user.username,
        'email': user.email
    }