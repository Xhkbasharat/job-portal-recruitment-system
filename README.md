💼 Job Portal & Recruitment Management System

Connecting Talent with Opportunities Through Technology

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=22&duration=3000&pause=900&color=00E5FF&center=true&vCenter=true&width=850&lines=Modern+Job+Portal+Web+Application;Smart+Job+Discovery+%26+Recruitment;Dedicated+Dashboards+for+Every+Role;Built+with+Python+%26+Flask" alt="Animated project tagline" />
</p><p align="center">
  <img src="https://img.shields.io/badge/Project-Full--Stack%20Web%20App-00E5FF?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Backend-Python%20%7C%20Flask-8A2BE2?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/Database-SQLite%20%7C%20MySQL-00C853?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Frontend-Bootstrap-orange?style=for-the-badge&logo=bootstrap&logoColor=white" />
</p><p align="center">
  <b>One platform. Three roles. A smarter recruitment experience.</b>
</p>---

🌐 Project Overview

The Job Portal & Recruitment Management System is a full-stack web application designed to simplify the recruitment process by connecting job seekers, recruiters, and administrators through a centralized platform.

Job seekers can discover opportunities, explore job details, and submit applications. Recruiters can publish job openings, manage applicants, and update application statuses. Administrators can oversee users and job listings through a dedicated management dashboard.

Built using Python, Flask, SQLAlchemy, and modern web technologies, the application demonstrates role-based workflows and database-driven web development.

🎯 Project Objectives

- Create a centralized platform for job discovery and recruitment.
- Provide separate experiences for job seekers and recruiters.
- Enable recruiters to publish and manage job vacancies.
- Simplify the job application process.
- Track application progress and status.
- Provide administrators with platform management tools.
- Build a responsive and user-friendly interface.

---

✨ Key Features

👨‍💼 Job Seeker Dashboard

- User registration and login.
- Browse available job opportunities.
- Search jobs by title, company, or location.
- View detailed job descriptions.
- Apply for available positions.
- Access a personalized dashboard.
- Track submitted applications and their statuses.

🏢 Recruiter Dashboard

- Recruiter registration and authentication.
- Create and publish job listings.
- Manage posted vacancies.
- View applicants for individual jobs.
- Review candidate applications.
- Update application statuses.
- Manage recruitment activities through a dedicated dashboard.

🛡️ Admin Dashboard

- Administrative dashboard.
- Manage registered users.
- Manage job listings.
- Activate or deactivate job postings.
- Delete user accounts.
- Monitor platform activity.

🔐 Authentication & Access Management

- User registration and login.
- Role-based access for job seekers, recruiters, and administrators.
- Password hashing using Flask-Bcrypt.
- Session management using Flask-Login.
- Protected application routes.

---

🔄 Application Workflow

                 ┌─────────────────────┐
                 │      Job Portal     │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │  User Registration  │
                 │     & Login         │
                 └──────────┬──────────┘
                            │
                 ┌──────────▼──────────┐
                 │   Role Selection    │
                 └──────────┬──────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
    ┌─────▼─────┐     ┌─────▼─────┐     ┌─────▼─────┐
    │Job Seeker │     │ Recruiter │     │   Admin   │
    └─────┬─────┘     └─────┬─────┘     └─────┬─────┘
          │                 │                 │
    ┌─────▼─────┐     ┌─────▼─────┐     ┌─────▼─────┐
    │ Search &  │     │ Post &    │     │ Manage    │
    │ Apply     │     │ Manage    │     │ Users &   │
    │ for Jobs  │     │ Jobs      │     │ Jobs      │
    └─────┬─────┘     └─────┬─────┘     └───────────┘
          │                 │
          └────────┬────────┘
                   │
          ┌────────▼────────┐
          │ Application     │
          │ Management      │
          └────────┬────────┘
                   │
          ┌────────▼────────┐
          │ Status Tracking │
          └─────────────────┘

---

🧰 Technology Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,bootstrap,js,sqlite,mysql,git,github" alt="Technology stack icons" />
</p>Category| Technologies
Programming Language| Python
Backend Framework| Flask
ORM| Flask-SQLAlchemy
Authentication| Flask-Login
Password Security| Flask-Bcrypt
Database Migrations| Flask-Migrate
Database Connectivity| PyMySQL
Database| SQLite (default), MySQL support
Frontend| HTML5, CSS3, JavaScript
UI Framework| Bootstrap
Version Control| Git, GitHub

---

🏗️ System Architecture

The application follows a modular Flask architecture with separate responsibilities for routing, database operations, authentication, and frontend rendering.

                ┌──────────────────────┐
                │      Frontend        │
                │ HTML / CSS / JS      │
                │     Bootstrap        │
                └──────────┬───────────┘
                           │
                ┌──────────▼───────────┐
                │     Flask Backend    │
                │  Routes & Controllers│
                └──────────┬───────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
    ┌─────▼─────┐    ┌─────▼─────┐    ┌─────▼─────┐
    │   Auth    │    │   Jobs    │    │Applications│
    │ Management│    │ Management│    │ Management │
    └─────┬─────┘    └─────┬─────┘    └─────┬──────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
                ┌──────────▼───────────┐
                │  Flask-SQLAlchemy    │
                │    Data Layer        │
                └──────────┬───────────┘
                           │
                ┌──────────▼───────────┐
                │      Database       │
                │    SQLite / MySQL   │
                └──────────────────────┘

---

📁 Project Structure

The following is a representative organization for the application. Adjust it to match the actual repository files.

job-portal-recruitment-system/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── jobs.py
│   │   ├── recruiter.py
│   │   ├── seeker.py
│   │   └── admin.py
│   │
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── extensions.py
│
├── migrations/
├── config.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md

---

🚀 Installation & Setup

1. Clone the Repository

git clone https://github.com/Xhkbasharat/job-portal-recruitment-system.git
cd job-portal-recruitment-system

2. Create a Virtual Environment

python -m venv venv

Activate the environment:

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure the Application

Set the required environment variables, including a secure Flask secret key and database connection details, according to the project's configuration.

5. Initialize the Database

Run the database initialization or migration commands specified by the application.

6. Start the Application

Use the actual Flask application entry point configured in the repository. For example:

python run.py

The entry-point filename and database initialization steps may differ depending on the current repository structure.

---

🔐 Security Considerations

The application uses Flask-Login for session-based authentication and Flask-Bcrypt for password hashing.

Before production deployment, additional security measures should be verified and configured:

- CSRF protection for form submissions.
- Secure session and cookie settings.
- Environment-based secret management.
- Server-side input validation.
- Role-based authorization checks on every protected operation.
- Database access controls.
- Secure production deployment configuration.

---

🗺️ Future Enhancements

Potential improvements for future versions include:

- Resume upload and parsing.
- Advanced job filtering.
- Email notifications for application updates.
- Candidate profile management.
- Recruiter analytics and recruitment insights.
- Interview scheduling.
- Job recommendation engine.
- Application status notifications.
- Automated testing and deployment pipelines.
- Improved accessibility and responsive UI.

---

💡 What This Project Demonstrates

This project brings together several important full-stack development concepts:

- Python backend development using Flask.
- Database modeling and ORM integration.
- Authentication and role-based application workflows.
- CRUD operations and data management.
- Job discovery and application management.
- Recruiter and administrator dashboards.
- Frontend and backend integration.
- Practical software architecture.

---

👨‍💻 Author

Sheikh Basharat Akbar

AI Writer at Mercor | AI Trainer at micro1 | AI/ML & Software Engineer

MCA Graduate — Islamic University of Science & Technology

Interests: Python Development, Software Engineering, Artificial Intelligence, Machine Learning, Web Applications, and Backend Systems.

<p align="center">
  <a href="https://www.linkedin.com/in/sheikh-basharat-389980225/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://github.com/Xhkbasharat">
    <img src="https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>---

⭐ Support the Project

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.

Feedback, suggestions, and contributions are welcome.

<p align="center">
  <b>Job Portal & Recruitment Management System</b><br/>
  <i>Bridging talent and opportunity through technology.</i>
</p><p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00E5FF,50:6A00F4,100:00C853&height=110&section=footer" width="100%" />
</p>
