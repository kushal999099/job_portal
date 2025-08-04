# app/employer.py
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app import db
from app.models import Job, Application

employer_bp = Blueprint('employer', __name__, url_prefix='/dashboard/employer')

@employer_bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'employer':
        return "Unauthorized", 403
    jobs = Job.query.filter_by(employer_id=current_user.id).all()
    return render_template('dashboard_employer.html', jobs=jobs)

@employer_bp.route('/post-job', methods=['GET', 'POST'])
@login_required
def post_job():
    if current_user.role != 'employer':
        return "Unauthorized", 403

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        salary = request.form['salary']
        job = Job(title=title, description=description, salary=salary,employer_id=current_user.id)
        db.session.add(job)
        db.session.commit()
        return redirect(url_for('employer.dashboard'))
    
    return render_template('post_job.html')


@employer_bp.route('/applications/<int:job_id>')
@login_required
def view_applications(job_id):
    if current_user.role != 'employer':
        return "Unauthorized", 403

    jobs = Job.query.filter_by(employer_id=current_user.id).all()
    job_ids = [job.id for job in jobs]
    applications = Application.query.filter(Application.job_id.in_(job_ids)).all()
    return render_template('applications_list.html', applications=applications)


@employer_bp.route('/delete-job/<int:job_id>', methods=['POST', 'GET'])
@login_required
def delete_job(job_id):
    if current_user.role != 'employer':
        return "Unauthorized", 403

    job = Job.query.get_or_404(job_id)
    if job.employer_id != current_user.id:
        return "Unauthorized", 403

    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('employer.dashboard'))
