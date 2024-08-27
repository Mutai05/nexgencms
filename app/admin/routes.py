from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.admin import admin
from app.blog.models import Post


@admin.route('/')
@login_required
def index():
    return render_template('admin/index.html')

@admin.route('/pages')
@login_required
def pages():
    return render_template('admin/pages.html', posts=posts)

@admin.route('/posts')
@login_required
def posts():
    posts = Post.query.all()
    return render_template('admin/posts.html', posts=posts)

@admin.route('/services')
@login_required
def services():
    return render_template('admin/services.html')

@admin.route('/post-count')
def post_count():
    post_count = Post.query.count()
    return render_template('admin/admin.html', post_count=post_count)

@admin.route('/settings')
@login_required
def settings():
    return render_template('admin/settings.html')

@admin.route('/enquiries')
@login_required
def enquiries():
    return render_template('admin/enquiries.html')
