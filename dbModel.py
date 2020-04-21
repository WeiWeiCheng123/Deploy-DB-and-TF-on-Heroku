from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tvlnxprmwxzwan:74c73bfe3c416cc5d0eb529c60e6e8619758976ec0faf2f2e415a8dcde47b1ba@ec2-3-231-46-238.compute-1.amazonaws.com:5432/d1avoq1j5ic1nh'
放你的資料庫URL
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
