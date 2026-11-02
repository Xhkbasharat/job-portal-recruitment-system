
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.job import Job
from models.application import Application

jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/jobs")
def jobs_list():
    search = request.args.get("search", "").strip()
    location = request.args.get("location", "").strip()

    query = Job.query.filter_by(is_active=True)

    if search:
        query = query.filter(
            db.or_(
                Job.title.ilike(f"%{search}%"),
                Job.company.ilike(f"%{search}%")
            )
        )

    if location:
        query = query.filter(
            Job.location.ilike(f"%{location}%")
        )

    jobs = query.order_by(Job.created_at.desc()).all()

    return render_template("jobs.html", jobs=jobs)


@jobs_bp.route("/jobs/<int:job_id>")
def job_detail(job_id):
    job = Job.query.filter_by(
        id=job_id,
        is_active=True
    ).first_or_404()

    return render_template("job_detail.html", job=job)


@jobs_bp.route("/apply/<int:job_id>", methods=["POST"])
@login_required
def apply_job(job_id):
    if current_user.role != "job_seeker":
        flash("Only job seekers can apply for jobs.", "danger")
        return redirect(url_for("jobs.jobs_list"))

    job = Job.query.filter_by(
        id=job_id,
        is_active=True
    ).first_or_404()

    existing_application = Application.query.filter_by(
        applicant_id=current_user.id,
        job_id=job.id
    ).first()

    if existing_application:
        flash("You have already applied for this job.", "warning")
        return redirect(url_for("jobs.job_detail", job_id=job.id))

    application = Application(
        applicant_id=current_user.id,
        job_id=job.id,
        cover_letter=request.form.get("cover_letter", "").strip()
    )

    db.session.add(application)
    db.session.commit()

    flash("Your application was submitted successfully!", "success")

    return redirect(url_for("jobs.dashboard"))


@jobs_bp.route("/dashboard")
@login_required
def dashboard():
    if current_user.role != "job_seeker":
        flash("Access denied.", "danger")
        return redirect(url_for("home"))

    applications = Application.query.filter_by(
        applicant_id=current_user.id
    ).order_by(Application.applied_at.desc()).all()

    return render_template(
        "dashboard.html",
        applications=applications
  )
  
