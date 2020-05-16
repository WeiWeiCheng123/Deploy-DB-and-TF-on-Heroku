from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xxxxxx'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class FileContents(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    data = db.Column(db.LargeBinary)

    def __init__(self
                , name
                , data
                ):
         self.name = name
         self.data = 	data

if __name__ == '__main__':
    manager.run()
