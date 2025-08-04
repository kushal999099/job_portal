# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobportal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

from app import models, auth, admin, employer, jobseeker

app.register_blueprint(auth.auth_bp)
app.register_blueprint(admin.admin_bp)
app.register_blueprint(employer.employer_bp)
app.register_blueprint(jobseeker.jobseeker_bp)
