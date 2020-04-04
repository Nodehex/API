import os
from flask import Flask
from flask_cors import CORS, cross_origin

from .blueprints.webhooks.apihook import apihook
from .blueprints.webhooks.websitehook import websitehook
from .blueprints.webhooks.dashboardhook import dashboardhook

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config['DATAPIPELINE_MERGE'] = os.environ.get('DATAPIPELINE_MERGE')
  app.config['DATAPIPELINE_PATH'] = os.environ.get('DATAPIPELINE_PATH')
  app.config['WEBSITE_MERGE'] = os.environ.get('WEBSITE_MERGE')
  app.config['WEBSITE_PATH'] = os.environ.get('WEBSITE_PATH')
  app.config['DASHBOARD_MERGE'] = os.environ.get('DASHBOARD_MERGE')
  app.config['DASHBOARD_PATH'] = os.environ.get('DASHBOARD_PATH')
  app.register_blueprint(apihook)
  app.register_blueprint(websitehook)
  app.register_blueprint(dashboardhook)

  return(app)