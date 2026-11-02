
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from extensions import db
from models.user import User
from models.job import Job
from models.application import Application

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


def admin_required():
    if current_user.role != "admin":
        flash("Administrator access required.", "danger")
        return False
    return True


@admin_bp.route("/dashboard")
@login_required
def dashboard():
    if not admin_required():
        return redirect(url_for("home"))

    total_users = User.query.count()
    total_jobs = Job.query.count()
    total_applications = Application.query.count()

    total_recruiters = User.query.filter_by(
        role="recruiter"
    ).count()

    total_job_seekers = User.query.filter_by(
        role="job_seeker"
    ).count()

    recent_jobs = Job.query.order_by(
        Job.created_at.desc()
    ).limit(5).all()

    return render_template(
        "admin_dashboard.html",
        total_users=total_users,
        total_jobs=total_jobs,
        total_applications=total_applications,
        total_recruiters=total_recruiters,
        total_job_seekers=total_job_seekers,
        recent_jobs=recent_jobs
    )


@admin_bp.route("/users")
@login_required
def manage_users():
    if not admin_required():
        return redirect(url_for("home"))

    users = User.query.order_by(
        User.created_at.desc()
    ).all()

    return render_template("manage_users.html", users=users)


@admin_bp.route("/jobs")
@login_required
def manage_jobs():
    if not admin_required():
        return redirect(url_for("home"))

    jobs = Job.query.order_by(
        Job.created_at.desc()
    ).all()

    return render_template("manage_jobs.html", jobs=jobs)


@admin_bp.route("/job/<int:job_id>/toggle", methods=["POST"])
@login_required
def toggle_job(job_id):
    if not admin_required():
        return redirect(url_for("home"))

    job = db.session.get(Job, job_id)

    if not job:
        flash("Job not found.", "danger")
        return redirect(url_for("admin.manage_jobs"))

    job.is_active = not job.is_active
    db.session.commit()

    flash("Job status updated successfully.", "success")
    return redirect(url_for("admin.manage_jobs"))


@admin_bp.route("/user/<int:user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    if not admin_required():
        return redirect(url_for("home"))

    user = db.session.get(User, user_id)

    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("admin.manage_users"))

    if user.id == current_user.id:
        flash("You cannot delete your own account.", "danger")
        return redirect(url_for("admin.manage_users"))

    if user.role == "admin":
        flash("Admin accounts cannot be deleted here.", "danger")
        return redirect(url_for("admin.manage_users"))

    db.session.delete(user)
    db.session.commit()

    flash("User deleted successfully.", "success")
    return redirect(url_for("admin.manage_users"))
  
