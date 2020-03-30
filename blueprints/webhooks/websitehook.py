from .helpers import validate_secret, handle_repository_update
from flask import request, Blueprint, jsonify

websitehook = Blueprint('websitehook', __name__, url_prefix='/api')

@websitehook.route('/websitehook', methods=['POST']) 
def handle_github_hook():

  if validate_secret(request, 'WEBSITE_MERGE'):
    pullrequest = request.json
    if 'pull_request' in pullrequest:
      handle_repository_update(pullrequest, 'WEBSITE_PATH')

  return jsonify({}), 200