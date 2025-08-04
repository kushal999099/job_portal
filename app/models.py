# app/models.py
from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # admin, employer, jobseeker

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    salary = db.Column(db.Float, nullable=True)  # Add this if missing
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    jobseeker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(50), default='Pending')  # Optional
    job = db.relationship('Job', backref='applications')
    jobseeker = db.relationship('User', backref='applications', foreign_keys=[jobseeker_id])
