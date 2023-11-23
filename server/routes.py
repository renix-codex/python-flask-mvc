from flask import Flask, jsonify, abort
from controllers import users, posts, list_all_users, get_post_by_id

app = Flask(__name__)

@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = list_all_users()
    return jsonify(posts)

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = get_post_by_id(post_id)
    if post:
        return jsonify(post)
    else:
        abort(404, "Post not found")