from .helpers import validate_secret, handle_repository_update
from flask import request, Blueprint, jsonify

apihook = Blueprint('apihook', __name__, url_prefix='/api')

@apihook.route('/apihook', methods=['POST']) 
def handle_github_hook():

  if validate_secret(request, 'DATAPIPELINE_MERGE'):
    pullrequest = request.json
    if 'pull_request' in pullrequest:
      handle_repository_update(pullrequest, 'DATAPIPELINE_PATH')

  return jsonify({}), 200

