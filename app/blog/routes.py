from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import os
from app.blog import blog
from app import db
from app.blog.models import Post
from flask_login import login_required, current_user

# New post

@blog.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        image_filename = request.form.get('image_filename')

        if not image_filename:
            flash('No image selected.', 'warning')

        # Create a new Post object with the current user's ID
        new_post = Post(title=title, content=content, image_filename=image_filename, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('admin.posts'))

    # Fetch list of uploaded images
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('new_post.html', files=files)