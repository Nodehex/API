import hmac
from flask import request, Blueprint, jsonify, current_app 
from git import Repo

websitehook = Blueprint('websitehook', __name__, url_prefix='/api')

def handle_repository_update(pullrequest):
  if pullrequest['action'] == 'closed' and pullrequest['pull_request']['merged']:
      repo = Repo(current_app.config.get('WEBSITE_PATH')) 
      origin = repo.remotes.origin 
      origin.pull()
      print('Repository updated with pull request {}'.format(pullrequest['pull_request']['head']['label']))

@websitehook.route('/websitehook', methods=['POST']) 
def handle_github_hook():

  signature = request.headers.get('X-Hub-Signature') 
  sha, signature = signature.split('=')

  secret = str.encode(current_app.config.get('WEBSITE_MERGE'))
  hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
  if hmac.compare_digest(hashhex, signature):
    pullrequest = request.json
    if 'action' in pullrequest:
      handle_repository_update(pullrequest)

  return jsonify({}), 200