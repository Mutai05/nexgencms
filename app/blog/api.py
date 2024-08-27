from flask import Blueprint, jsonify, request, abort
from app import db
from app.blog.models import Post

api = Blueprint('api', __name__)

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

@api.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(post.to_dict())
