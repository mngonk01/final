from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import sys
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_pyfile('config.py')
app.config.from_object('config')


db = SQLAlchemy(app)



migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command(db, MigrateCommand)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    #q:pets = db.relationship('pet', backref='owner', lazy='dynamic')


if __name__ =='__main__':
    manager.run()
