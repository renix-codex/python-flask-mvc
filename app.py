from flask import *
import flask
from models import User
from controllers import users, posts, get_user_by_username, get_post_by_id, get_comments_for_post
from middleware import AuthorizationMiddleware

app = Flask(__name__)

# Add your authorized tokens here (replace with your actual tokens)
authorized_tokens = ['your_secret_token']

# Use the authorization middleware
app.wsgi_app = AuthorizationMiddleware(app.wsgi_app, authorized_tokens)

# REST API routes
@app.route('/api/posts', methods=['GET'])
def get_posts():
    # Your logic to retrieve and return posts
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        return jsonify(post)
    else:
        abort(404, "Post not found")

# Add more routes for creating, updating, and deleting posts

if __name__ == '__main__':
    app.run(debug=True)
