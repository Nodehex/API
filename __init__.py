import os
from flask import Flask
from flask_cors import CORS, cross_origin

from .api import api
from .apihook import apihook
from .websitehook import websitehook

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['DATAPIPELINE_MERGE'] = os.environ.get('DATAPIPELINE_MERGE')
  app.config['DATAPIPELINE_PATH'] = os.environ.get('DATAPIPELINE_PATH')
  app.config['WEBSITE_MERGE'] = os.environ.get('WEBSITE_MERGE')
  app.config['WEBSITE_PATH'] = os.environ.get('WEBSITE_PATH')
  app.register_blueprint(apihook)
  app.register_blueprint(websitehook)
  app.register_blueprint(api)

  return(app)