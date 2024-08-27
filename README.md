# NexgenCMS

NEXGENCMS is a content management system (CMS) built with Flask, a lightweight web framework for Python.
It is designed to manage and display blog posts, handle media uploads, generate invoices, and more. This README provides an overview of the project's features, technologies used, installation instructions, and areas for future improvement. It utilizes various technologies for both frontend and backend development to create a responsive and feature-rich web application.

## Project Structure

```
nexgencms/
│
├── app/
│   ├── admin/            # Admin dashboard and management interface
│   │   ├── routes.py     # Routes for admin functionalities
│   │   ├── __init__.py   # Admin blueprint initialization
│   │   ├── static/       # Static files for admin (JS, CSS, images)
│   │   └── templates/    # HTML templates for admin views
│   ├── blog/             # Blog management
│   │   ├── routes.py     # Routes for blog functionalities
│   │   ├── __init__.py   # Blog blueprint initialization
│   │   ├── static/       # Static files for blog (CSS, images)
│   │   └── templates/    # HTML templates for blog views
│   ├── core/             # Core site functionalities (home, about, contact, etc.)
│   │   ├── routes.py     # Routes for core functionalities
│   │   ├── __init__.py   # Core blueprint initialization
│   │   ├── static/       # Static files for core (JS, CSS, images)
│   │   └── templates/    # HTML templates for core views
│   ├── media/            # Media file management
│   │   ├── routes.py     # Routes for media functionalities
│   │   ├── __init__.py   # Media blueprint initialization
│   │   ├── static/       # Static files for media (CSS)
│   │   └── templates/    # HTML templates for media views
│   ├── invoices/         # Invoice management
│   │   ├── routes.py     # Routes for invoice functionalities
│   │   ├── __init__.py   # Invoices blueprint initialization
│   │   ├── static/       # Static files for invoices (JS, CSS, images)
│   │   └── templates/    # HTML templates for invoice views
│   ├── database/         # Database management tools
│   │   ├── routes.py     # Routes for database functionalities
│   │   ├── __init__.py   # Database blueprint initialization
│   │   ├── static/       # Static files for database (CSS)
│   │   └── templates/    # HTML templates for database views
│   ├── __init__.py       # Flask app initialization
│   ├── config.py         # Configuration settings for the app
│   ├── migrations/       # Database migrations
│   └── static/           # Static files shared across the app
│
├── instance/             # Instance-specific configuration files
├── __pycache__/          # Compiled Python files
├── run.py                # Entry point to run the Flask app
└── venv/                 # Virtual environment
```

## Technologies Used

### Backend

- **Python**: Programming language for backend development.
- **Flask**: Lightweight WSGI web application framework.
- **SQLAlchemy**: ORM for managing database interactions.
- **MySQL**: Relational database system used for storing application data.
- **Flask-Login**: For user session management.
- **Flask-Migrate**: For handling database migrations.
- **Bcrypt**: For password hashing.

### Frontend

- **HTML**: Structure of web pages.
- **CSS**: Styling of web pages. Includes custom styles and Bootstrap for responsive design.
- **JavaScript**: Adding interactivity to web pages. Includes libraries such as jQuery and various plugins (e.g., Lightbox, Owl Carousel).
- **Bootstrap**: CSS framework for responsive design.
- **CKEditor**: WYSIWYG editor for rich text content.

## Routes

### Admin Blueprint

- `/admin/dashboard`: Displays the admin dashboard.
- `/admin/posts`: Manages blog posts.
- `/admin/pages`: Manages static pages.
- `/admin/settings`: Manages site settings.
- `/admin/enquiries`: Manages user enquiries.
- `/admin/services`: Manages services offered by the site.

### Blog Blueprint

- `/blog/new_post`: Creates a new blog post.
- `/blog/edit_post/<int:post_id>`: Edits an existing blog post.
- `/blog/single_post/<int:post_id>`: Displays a single blog post.
- `/blog/posts_base`: Displays a list of all blog posts.

### Core Blueprint

- `/`: Home page of the site.
- `/about`: About page.
- `/contact`: Contact page.
- `/services`: Services page.
- `/faqs`: Frequently asked questions page.
- `/quote`: Request a quote page.

### Media Blueprint

- `/media/upload`: Uploads media files.
- `/media/gallery`: Displays the media gallery.

### Invoices Blueprint

- `/invoices/list`: Lists all invoices.
- `/invoices/view/<int:invoice_id>`: Views a single invoice.
- `/invoices/new`: Creates a new invoice.
- `/invoices/pdf/<int:invoice_id>`: Generates a PDF for an invoice.

### Database Blueprint

- `/database/details`: Displays database details.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/nexgencms.git
   cd nexgencms
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database and apply migrations:

   ```bash
   flask db upgrade
   ```

5. Run the application:
   ```bash
   python run.py
   ```

## Usage

- Open your browser and go to `http://127.0.0.1:5000` to view the application.

## Room for Improvement

1. Enhanced Security: Implement additional security measures, such as two-factor authentication.

2. User Roles and Permissions: Add role-based access control to manage different user permissions.

3. API Documentation: Provide comprehensive API documentation for easier integration.

4. Automated Testing: Develop automated tests for better reliability and maintainability.

5. Front-End Improvements: Enhance the UI/UX with modern JavaScript frameworks or libraries.

6. Internationalization: Add support for multiple languages.

7. Performance Optimization: Optimize database queries and application performance.

## Contributing

If you would like to contribute to the project, please fork the repository and submit a pull request. For bug reports or feature requests, open an issue in the GitHub repository.

## License

This project is licensed under the MIT License.
