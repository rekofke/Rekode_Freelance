from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=True, nullable=False) # store hashed
    name = db.Column(db.String(100), unique=True, nullable=False)
    clients = db.relationship('Client', backref='user', lazy=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    projects = db.relationship('Project', backref='client', lazy=True)
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hourly_rate = db.Column(db.Float, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    time_entries = db.relationship('TimeEntry', backref='project',lazy=True)

class TimeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200))
    hours = db.Column(db.Float, nullable=False)
    date  = db.Column(db.Date, default=datetime.utcnow)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    invoiced = db.Column(db.Boolean, default=False)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=True)
    

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column (db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    issue_date = db.Column(db.Date, default=datetime.utcnow)
    due_date = db.Column(db.Date)
    total_amount = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    time_entries = db.relationship('TimeEntry', backref='invoice', lazy=True)
