import os
from flask import Flask
from flask_cors import CORS, cross_origin

from .api import api
from .webhooks import webhook

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['DATAPIPELINE_MERGE'] = os.environ.get('DATAPIPELINE_MERGE')
  app.config['REPO_PATH'] = os.environ.get('REPO_PATH')
  app.register_blueprint(webhook)
  app.register_blueprint(api)

  return(app)