import hmac
from flask import request, current_app
from git import Repo

def handle_repository_update(pullrequest, config_name):
  if pullrequest['action'] == 'closed' and pullrequest['pull_request']['merged']:
      repo = Repo(current_app.config.get(config_name)) 
      origin = repo.remotes.origin 
      origin.pull()
      print('Repository updated with pull request {}'.format(pullrequest['pull_request']['head']['label']))


def validate_secret(req, config_name):
    signature = req.headers.get('X-Hub-Signature') 
    sha, signature = signature.split('=')

    secret = str.encode(current_app.config.get(config_name))
    hashhex = hmac.new(secret, req.data, digestmod='sha1').hexdigest()
    return hmac.compare_digest(hashhex, signature)