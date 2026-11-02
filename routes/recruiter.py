
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.job import Job
from models.application import Application

recruiter_bp = Blueprint("recruiter", __name__, url_prefix="/recruiter")


def recruiter_required():
    if current_user.role != "recruiter":
        flash("Recruiter access required.", "danger")
        return False
    return True


@recruiter_bp.route("/dashboard")
@login_required
def dashboard():
    if not recruiter_required():
        return redirect(url_for("home"))

    jobs = Job.query.filter_by(
        recruiter_id=current_user.id
    ).order_by(Job.created_at.desc()).all()

    return render_template("recruiter_dashboard.html", jobs=jobs)


@recruiter_bp.route("/post-job", methods=["GET", "POST"])
@login_required
def post_job():
    if not recruiter_required():
        return redirect(url_for("home"))

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        company = request.form.get("company", "").strip()
        location = request.form.get("location", "").strip()
        job_type = request.form.get("job_type", "").strip()
        description = request.form.get("description", "").strip()
        requirements = request.form.get("requirements", "").strip()
        salary = request.form.get("salary", "").strip()

        if not all([title, company, location, job_type, description]):
            flash("Please complete all required fields.", "danger")
            return redirect(url_for("recruiter.post_job"))

        job = Job(
            title=title,
            company=company,
            location=location,
            job_type=job_type,
            salary=salary,
            description=description,
            requirements=requirements,
            recruiter_id=current_user.id
        )

        db.session.add(job)
        db.session.commit()

        flash("Job posted successfully!", "success")
        return redirect(url_for("recruiter.dashboard"))

    return render_template("post_job.html")


@recruiter_bp.route("/applicants/<int:job_id>")
@login_required
def applicants(job_id):
    if not recruiter_required():
        return redirect(url_for("home"))

    job = Job.query.filter_by(
        id=job_id,
        recruiter_id=current_user.id
    ).first_or_404()

    applications = Application.query.filter_by(
        job_id=job.id
    ).order_by(Application.applied_at.desc()).all()

    return render_template(
        "applicants.html",
        job=job,
        applications=applications
    )


@recruiter_bp.route(
    "/application/<int:application_id>/status",
    methods=["POST"]
)
@login_required
def update_application_status(application_id):
    if not recruiter_required():
        return redirect(url_for("home"))

    application = db.session.get(Application, application_id)

    if not application or application.job.recruiter_id != current_user.id:
        flash("Application not found.", "danger")
        return redirect(url_for("recruiter.dashboard"))

    status = request.form.get("status", "")

    allowed_statuses = [
        "Pending",
        "Reviewed",
        "Shortlisted",
        "Rejected",
        "Accepted"
    ]

    if status not in allowed_statuses:
        flash("Invalid application status.", "danger")
        return redirect(
            url_for("recruiter.applicants", job_id=application.job_id)
        )

    application.status = status
    db.session.commit()

    flash("Application status updated.", "success")

    return redirect(
        url_for("recruiter.applicants", job_id=application.job_id)
  )
  
