from flask import Flask
from flask_migrate import Migrate 
from models import db, Customer
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

migrate = Migrate(app, db)
db.init_app(app)
