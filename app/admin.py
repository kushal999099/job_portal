# app/admin.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Job, User, Application
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/dashboard/admin')

@admin_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return "Unauthorized", 403

    jobs_count = Job.query.count()
    employers_count = User.query.filter_by(role='employer').count()
    jobseekers_count = User.query.filter_by(role='jobseeker').count()
    applications_count = Application.query.count()

    return render_template('dashboard_admin.html', 
                           jobs=jobs_count, 
                           employers=employers_count,
                           jobseekers=jobseekers_count,
                           applications=applications_count)
