# app/jobseeker.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Job, Application
from app import db

jobseeker_bp = Blueprint('jobseeker', __name__, url_prefix='/dashboard/jobseeker')

@jobseeker_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'jobseeker':
        return "Unauthorized", 403
    applied = Application.query.filter_by(jobseeker_id=current_user.id).all()
    print(applied, 'ffff')
    return render_template('dashboard_jobseeker.html', applications=applied)

@jobseeker_bp.route('/jobs')
@login_required
def jobs_list():
    if current_user.role != 'jobseeker':
        return "Unauthorized", 403
    
    jobs = Job.query.all()
    return render_template('jobs_list.html', jobs=jobs)

@jobseeker_bp.route('/apply/<int:job_id>')
@login_required
def apply(job_id):
    if current_user.role != 'jobseeker':
        return "Unauthorized", 403
    already_applied = Application.query.filter_by(job_id=job_id, jobseeker_id=current_user.id).first()
    if already_applied:
        return "Already applied!"
    application = Application(job_id=job_id, jobseeker_id=current_user.id)
    db.session.add(application)
    db.session.commit()
    return redirect(url_for('jobseeker.dashboard'))
