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
    return render_template('blog/new_post.html', files=files)

# Edit post

@blog.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        post.title = request.form.get('title')
        post.content = request.form.get('content')
        image_filename = request.form.get('image_filename')  # Ensure this matches your form field
        
        if image_filename:
            post.image_filename = image_filename
        
        db.session.commit()
        flash('Post has been updated successfully.', 'success')
        return redirect(url_for('admin.posts', post_id=post.id))
    
    # Fetch list of uploaded images
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('blog/edit_post.html', post=post, files=files)


# Delete post

@blog.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    
    db.session.delete(post)
    db.session.commit()
    
    flash('Post has been deleted successfully.', 'success')
    return redirect(url_for('admin.posts'))

# Single post

@blog.route('/post/<int:post_id>')
def single_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('blog/single_post.html', post=post)
