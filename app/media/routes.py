from flask import Blueprint, render_template, request, redirect, url_for, flash, send_from_directory, current_app
from werkzeug.utils import secure_filename
import os
from app.media import media
from flask_login import login_required

# Allowed files

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

# Upload files

@media.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        files = request.files.getlist('files[]')

        if not files:
            flash('No selected files')
            return redirect(request.url)

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        flash('Files successfully uploaded!', 'success')
        return redirect(url_for('media.gallery'))

    return render_template('upload.html')

# Files path

@media.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(os.path.join(current_app.root_path, 'static/uploads'), name)


#  Admin media gallery

@media.route('/')
@login_required
def gallery():
    # List all files in the upload folder
    files = os.listdir(current_app.config['UPLOAD_FOLDER'])
    return render_template('media.html', files=files)

# Delete media

@media.route('/delete/<name>', methods=['POST'])
@login_required
def delete_file(name):
    try:
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], name)
        if os.path.exists(file_path):
            os.remove(file_path)
            flash('File successfully deleted.', 'success')
        else:
            flash('File not found.', 'error')
    except Exception as e:
        flash(f'Error deleting file: {str(e)}', 'error')
    return redirect(url_for('media.gallery'))