import hmac
from flask import request, Blueprint, jsonify, current_app 
from git import Repo

webhook = Blueprint('webhook', __name__, url_prefix='')

@webhook.route('/datahook', methods=['POST']) 
def handle_github_hook():

  signature = request.headers.get('X-Hub-Signature') 
  sha, signature = signature.split('=')

  secret = str.encode(current_app.config.get('DATAPIPELINE_MERGE'))

  hashhex = hmac.new(secret, request.data, digestmod='sha1').hexdigest()
  if hmac.compare_digest(hashhex, signature):
    pullrequest = request.json
    if pullrequest['action'] == 'closed' and pullrequest['pull_request']['merged']:
      repo = Repo(current_app.config.get('REPO_PATH')) 
      origin = repo.remotes.origin 
      origin.pull()
      print('Repository updated with pull request {}'.format(pullrequest['pull_request']['head']['label']))

  return jsonify({}), 200