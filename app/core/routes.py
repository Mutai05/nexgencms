from flask import render_template
from app.core import core
from app.blog.models import Post

@core.route('/')
def index():
    return render_template('core/index.html')

@core.route('/about-us')
def about():
    return render_template('core/about.html', title='About Us')

@core.route('/our-services')
def services():
    return render_template('core/services.html', title='Our Services')

@core.route('/articles')
def articles():
    posts = Post.query.all()
    return render_template('core/blog.html', title='Blog', posts=posts)

@core.route('/faqs')
def faqs():
    return render_template('core/faqs.html', title='FAQs')

@core.route('/quote')
def quote():
    return render_template('core/quote.html', title='Get Quote')

@core.route('/contact-us')
def contact():
    return render_template('core/contact.html', title='Contact Us')