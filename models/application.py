
from datetime import datetime
from extensions import db


class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    applicant_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    job_id = db.Column(
        db.Integer,
        db.ForeignKey("jobs.id"),
        nullable=False
    )

    resume = db.Column(db.String(255))

    cover_letter = db.Column(db.Text)

    status = db.Column(
        db.String(30),
        default="Pending",
        nullable=False
    )

    applied_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    __table_args__ = (
        db.UniqueConstraint(
            "applicant_id",
            "job_id",
            name="unique_job_application"
        ),
    )

    def __repr__(self):
        return f"<Application {self.id}: {self.status}>"
      
