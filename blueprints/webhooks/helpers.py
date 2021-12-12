import hmac
import subprocess
import os
from flask import request, current_app
from contextlib import contextmanager

def change_directory(new_directory):
    old_directory = os.getcwd()
    os.chdir(new_directory)
    try:
        yield
    finally:
        os.chdir(old_directory)

def handle_repository_update(pullrequest, config_name):
  if pullrequest['action'] == 'closed' and pullrequest['pull_request']['merged']:
      with change_directory(current_app.config.get(config_name)):
          subprocess.run("git pull")

def validate_secret(req, config_name):
    signature = req.headers.get('X-Hub-Signature')
    sha, signature = signature.split('=')

    secret = str.encode(current_app.config.get(config_name))
    hashhex = hmac.new(secret, req.data, digestmod='sha1').hexdigest()
    return hmac.compare_digest(hashhex, signature)
