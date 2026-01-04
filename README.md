🏗️ Interior Designer Website (Django & FastAPI)
📖 Overview
This is an Interior Designer website built using Django for backend and FastAPI for handling some API endpoints. The project includes dynamic page routing, API integration, and a responsive frontend.

🚀 Features
✅ Dynamic Routing (Home, About, Services, Projects, Blog, Contact)
✅ FastAPI Integration for high-performance API handling
✅ Django Template System with Bootstrap for styling
✅ Database Integration using SQLite/PostgreSQL/MySQL
✅ AJAX & jQuery for smooth page interactions
✅ Contact Form with Email Integration
✅ Admin Panel for content management
🛠️ Tech Stack
Backend: Django, FastAPI
Frontend: HTML, CSS, Bootstrap, jQuery
Database: SQLite / MySQL / PostgreSQL
APIs: RESTful APIs using Django & FastAPI
Version Control: Git & GitHub
📂 Folder Structure

1. .git/

This is a hidden folder used by Git to track changes in your project.

You don’t need to modify anything here manually.

It contains all version history, branches, and commits.

2. ai_engine/

This folder likely contains your AI-related logic for the project.

Could include Python scripts for:

Generating content or suggestions for interiors.

Integrating ML/AI models.

APIs for AI services.

Think of this as the "brain" behind your AI features.

3. core/

Usually contains main app logic or settings that other apps depend on.

Likely includes:

models.py → database models used across multiple apps.

views.py → generic views or core functionality.

urls.py → core routing if not app-specific.

Sometimes also contains settings.py if you structured the project differently.

4. leads/

This app likely handles leads or potential clients.

Could include:

Forms for capturing lead info.

Views to display lead lists or details.

Models like Lead, Contact, or Inquiry.

This is where you’ll implement CRUD (Create, Read, Update, Delete) for leads.

5. media/

Used for user-uploaded files (like images or documents).

Typically defined in settings.py with:

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


Static images uploaded via forms go here.

6. portfolio/

Likely manages interior design projects or portfolio items.

Could include:

Models like PortfolioItem with images, descriptions.

Views to display portfolio items.

Admin interface to manage portfolio content.

7. projects/

Might be similar to portfolio, but perhaps actual client projects or internal projects.

Could have:

Project timelines, tasks, or statuses.

Models like Project with related client and portfolio info.

8. static/

Stores CSS, JS, and static images that your frontend uses.

Unlike media/, these are not uploaded by users, they are project assets.

9. templates/

Contains all HTML templates used in your project.

Django renders templates to generate UI.

Likely subfolders:

leads/ → templates related to lead forms or list views.

portfolio/ → templates for portfolio pages.

base.html → common layout for all pages.

10. manage.py

Django’s command-line utility.

Used to:

Run server: python manage.py runserver

Make migrations: python manage.py makemigrations

Apply migrations: python manage.py migrate

Create superuser: python manage.py createsuperuser

11. requirements.txt

Lists Python dependencies.

Install them with:

pip install -r requirements.txt

12. db.sqlite3

Your SQLite database file.

Stores all your models and data.

Very small (0 KB in your screenshot, maybe empty now).