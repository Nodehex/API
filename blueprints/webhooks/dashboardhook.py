from .helpers import validate_secret, handle_repository_update
from flask import request, Blueprint, jsonify

dashboardhook = Blueprint('dashboardhook', __name__, url_prefix='/api')

@dashboardhook.route('/dashboardhook', methods=['POST']) 
def handle_github_hook():

  if validate_secret(request, 'DASHBOARD_MERGE'):
    pullrequest = request.json
    if 'pull_request' in pullrequest:
      handle_repository_update(pullrequest, 'DASHBOARD_PATH')

  return jsonify({}), 200