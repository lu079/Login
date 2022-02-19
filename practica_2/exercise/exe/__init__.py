from flask import Flask
from exe import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app=Flask(__name__)
cors=CORS(app)
app.secret_key = os.urandom(24)
app.config['CORS_HEADERS']='Content-Type'

app.config.from_object(config.Config)
db=SQLAlchemy(app)

from exe import routers,models

