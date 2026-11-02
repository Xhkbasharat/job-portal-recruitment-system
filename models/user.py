
from datetime import datetime
from flask_login import UserMixin
from extensions import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
        index=True
    )

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.String(20),
        nullable=False,
        default="job_seeker"
    )

    phone = db.Column(db.String(20))

    company_name = db.Column(db.String(150))

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    jobs = db.relationship(
        "Job",
        backref="recruiter",
        lazy=True,
        cascade="all, delete-orphan"
    )

    applications = db.relationship(
        "Application",
        backref="applicant",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<User {self.email}>"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
                        
