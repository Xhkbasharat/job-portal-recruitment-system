
from datetime import datetime
from extensions import db


class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(150),
        nullable=False
    )

    company = db.Column(
        db.String(150),
        nullable=False
    )

    location = db.Column(
        db.String(150),
        nullable=False
    )

    job_type = db.Column(
        db.String(50),
        nullable=False
    )

    salary = db.Column(db.String(100))

    description = db.Column(
        db.Text,
        nullable=False
    )

    requirements = db.Column(db.Text)

    recruiter_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    deadline = db.Column(db.Date)

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    applications = db.relationship(
        "Application",
        backref="job",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Job {self.title}>"
      
